// This entry opens the full Windows app; it does not replace the pet with a reduced overlay.
window.__ModuleLoader__.load({id:'dsh-aemeath',factory(require){
  const React=require('react'),h=React.createElement;
  const {useState,useEffect}=React;
  const CSS=`.am-full{position:fixed;right:18px;bottom:238px;z-index:10000;font:15px/1.6 system-ui,'Microsoft YaHei',sans-serif;color:#eaf5ff;pointer-events:auto}.am-full *{box-sizing:border-box}.am-full button,.am-full select{font:inherit;color:inherit;background:#274767;border:1px solid #6c91b0;border-radius:10px;padding:8px 12px;cursor:pointer}.am-full button:disabled{opacity:.5;cursor:default}.am-full .am-card{width:min(410px,calc(100vw - 32px));max-height:calc(100vh - 110px);overflow:auto;background:#172c43;border:1px solid #6b9bc3;border-radius:18px;padding:22px;box-shadow:0 10px 45px #0008}.am-full h2{font-size:22px;margin:0 0 12px}.am-full p{margin:8px 0 14px}.am-full .am-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.am-full .am-open{display:flex;align-items:center;gap:8px;background:#172c43}.am-full img{width:32px;height:32px}.am-full .am-info{font-size:13px;color:#bfd4e9}.am-full .am-error{color:#ffd2c5;white-space:pre-wrap}.am-full select{width:100%;margin-top:6px}.am-full progress{width:100%}`;
  const SETTINGS_CSS=`.am-full.am-settings{position:static;font:inherit}.am-full.am-settings .am-card{width:min(680px,100%);max-height:none;box-shadow:none}.am-full .am-entry-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}`;
  function Entry({settingsPage=false}={}){
    const[open,setOpen]=useState(false),[state,setState]=useState(null),[error,setError]=useState(''),[source,setSource]=useState('auto'),[working,setWorking]=useState(false),[dismissed,setDismissed]=useState(false);
    useEffect(()=>{
      const abort=new AbortController();let active=true,fetching=false;
      async function poll(){if(fetching)return;fetching=true;try{
        const r=await fetch('aemeath-full/status',{credentials:'same-origin',signal:abort.signal});
        if(!r.ok)throw Error('无法连接桌宠插件');const value=await r.json();if(active)setState(value);
      }catch(e){if(active)setError(e.message);}finally{fetching=false;}}
      void poll();const timer=setInterval(poll,1000);return()=>{active=false;abort.abort();clearInterval(timer);};
    },[]);
    async function act(action){
      setWorking(true);setError('');try{
        const r=await fetch('aemeath-full/action',{method:'POST',credentials:'same-origin',headers:{'content-type':'application/json','x-aemeath-token':state.token},body:JSON.stringify({action,source})});
        const result=await r.json();if(!r.ok)throw Error(result.error||'操作失败');
        const status=await fetch('aemeath-full/status',{credentials:'same-origin'});
        if(status.ok)setState(await status.json());
      }catch(e){setError(e.message);}finally{setWorking(false);}
    }
    const busy=working||state?.busy;
    // An older program may have no one-click update, so an available update overrides the hidden entry.
    const updatePrompt=!settingsPage&&!!state?.needsUpdate;
    if(!settingsPage&&(!state&&!error||state?.entryHidden&&!updatePrompt))return null;
    return h('div',{className:settingsPage?'am-full am-settings':'am-full'},(open||settingsPage||updatePrompt&&!dismissed)?h('section',{className:'am-card','aria-label':'爱弥斯桌宠完整版'},
      h('h2',null,'爱弥斯 · 完整版'),
      h('p',null,'自选 GIF、语音字幕、播放规则、字体大小、锁定穿透和配置迁移，都在原来的桌宠设置里。'),
      h('p',{className:'am-info'},'Windows 10/11 x64 · 本机 Harness。桌宠可在桌面任意位置陪伴，三套表情预设（鸭牌、雾雪、Stephen）各配好 16 种交互，90 条爱弥斯语音（含字幕）和两款字体；更多表情包可从呜哇小站下载后导入。'),
      !state?h('p',null,'正在连接…'):!state.supported?h('p',{className:'am-error'},'此版本需要在 Windows x64 电脑上运行 Harness。'):h(React.Fragment,null,
        h('p',null,state.installed?`已安装 v${state.version}${state.running?' · 运行中':' · 已关闭'}`:`首次下载约 ${state.megabytes} MB，无需安装 Python。`),
        (!state.installed||state.needsUpdate)?h('label',null,'下载来源',h('select',{value:source,onChange:e=>setSource(e.target.value),disabled:busy},h('option',{value:'auto'},'自动选择'),h('option',{value:'github'},'GitHub 官方源'),h('option',{value:'mirror'},'镜像加速（GH-Proxy）'))):null,
        state.needsUpdate?h('p',null,`可安装 v${state.targetVersion}，仅下载程序更新，保留配置素材并自动重启。如果旧版桌宠也弹出更新窗口，请忽略它，在这里更新。`):null,
        state.busy?h('progress',{value:state.progress??0,max:100,'aria-label':'下载进度'}):null,
        state.message?h('p',{role:'status'},state.message):null,
        h('div',{className:'am-actions'},
          (!state.installed||state.needsUpdate)?h('button',{disabled:busy,onClick:()=>act('install')},state.installed?'更新并重启爱弥斯':'下载并安装完整版'):null,
          state.installed?h('button',{disabled:busy,onClick:()=>act('start')},state.running?'唤醒桌宠':'启动桌宠'):null,
          state.installed?h('button',{disabled:busy,onClick:()=>act('settings')},'打开完整设置'):null,
          state.running?h('button',{disabled:busy,onClick:()=>act('stop')},'关闭桌宠'):null)),
      error?h('p',{className:'am-error',role:'alert'},error):null,
      h('p',{className:'am-info'},'原独立版的配置素材 ZIP 可在「设置 → 保存与迁移」导入。个人素材保存在 Harness 数据目录，更新、卸载插件不会删除。'),
      h('p',{className:'am-info'},'以后也可右键桌宠 → 设置 → 版本与更新 → 一键更新，或点击常驻提醒中的“更新并重启爱弥斯”。'),
      h('p',{className:'am-info'},'安装并成功启动后，部署入口会自动隐藏，有程序更新时会重新显示。以后可在 Harness「设置 → 爱弥斯桌宠」管理或恢复入口。'),
      h('div',{className:'am-entry-actions'},
        !settingsPage?h('button',{onClick:()=>{setOpen(false);setDismissed(true);}},'收起面板'):null,
        state?.installed&&(settingsPage||!state.entryHidden)?h('button',{disabled:busy,onClick:()=>act(state.entryHidden?'show_entry':'hide_entry')},state.entryHidden?'显示部署入口':'隐藏部署入口'):null)
    ):h('button',{className:'am-open',onClick:()=>setOpen(true),'aria-label':'打开爱弥斯桌宠入口'},h('img',{src:'aemeath-full/icon.png',alt:''}),'爱弥斯桌宠'));
  }
  function apply(ctx){ctx.effect(()=>{
    const style=document.createElement('style');style.textContent=CSS+SETTINGS_CSS;document.head.appendChild(style);
    const dispose=ctx.slots.inject('shell.overlay',()=>ctx.slots.register({name:'shell.overlay',id:'aemeath-full',inject:()=>({})},Entry));
    const disposeSettings=ctx.slots.inject('settings.section',()=>ctx.slots.register({name:'settings.section',id:'aemeath-full',order:70,label:'爱弥斯桌宠',inject:()=>({settingsPage:true})},Entry));
    return()=>{disposeSettings?.();dispose?.();style.remove();};
  },'aemeath: full desktop entry');}
  return {apply,inject:['slots']};
}});
