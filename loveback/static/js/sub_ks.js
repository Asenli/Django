var onKST= function(text) {
	//请替换成"生成代码 - 链接地址" 中的链接地址,不要去其他地方复制
	ksChatLink = 'http://kf7.kuaishang.cn/bs/im.htm?cas=56293___998837&fi=66510';
	/**
	 * 若强行打开新窗口,则放开设置,不设置则手机不打开新窗口,pc打开新窗口,此设置只对当前自定义事件有效
	 * 若想全局生效,包括快商通默认的打开聊天窗口事件,则将此变量ksUserDefinedOpenNewChatWin定义在ks.j前即可
	 */
	//var ksUserDefinedOpenNewChatWin=true;	
	
	//验证参数是否存在
	function checkQueryString(params,name){
		if(!params)return false;
		return new RegExp("(^|&)"+ name +"=([^&]*)(&|$)", "i").test(params);
	}
	//获取URL参数值
	function getQueryString(url,name) {
		var index = url.indexOf('?');
		if(index==-1)return '';
		url=url.substr(index+1,url.length);
		var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
		var r = url.match(reg);
		if (r != null) return unescape(r[2]);
		return '';
	}
	var openNewChatWin;
	var localArr = ksChatLink.split("?");
	localArr.push("");
	if(typeof ksUserDefinedOpenNewChatWin!='undefined' && ksUserDefinedOpenNewChatWin==true){
		openNewChatWin = true;
	}else if(checkQueryString(localArr[1],'ism')){
		openNewChatWin = false;
	}else{
		openNewChatWin = true;
	}
	//打开快商通聊天窗口链接
	function ksOpenLink(){
		var appendTailUrl='';
		try{
			var cas = getQueryString(ksChatLink,'cas');
			if(cas){
				var vi='';
				var dc = document.cookie.match(new RegExp('(^| )' + cas+'_KS_'+cas + '=([^;]*)(;|$)'));
				if (dc != null){
					vi = unescape(dc[2]);
				}
				if(vi){
					appendTailUrl += '&vi='+vi;
				}
			}
		}catch(e){}
		var ref="";
		try{if(opener.document.referrer.length>0){ref=opener.document.referrer;}}catch(e){ref=document.referrer;}
		if(!ref || ref.length==0){ref=document.referrer;}
		//对话网址
		appendTailUrl += '&dp='+encodeURIComponent(window.location.href);
		//访客来源
		if(ref)appendTailUrl+='&ref='+encodeURIComponent(ref);
		//对话标识
		if(text)appendTailUrl+='&sText='+encodeURIComponent(text);
		if(ksChatLink.indexOf('?')==-1){appendTailUrl=appendTailUrl.substring(1)+'?';}
		ksChatLink+=appendTailUrl;
		//根据openNewChatWin设置打开聊天窗口
		if(!openNewChatWin){
			window.location.href=ksChatLink;
		}else{
			var ksWin = window.open(ksChatLink,'_blank');
			if(ksWin){
				try{ksWin.focus();}catch(e){} //将焦点定位到聊天窗口
			}
		}
	}
	//如果快商通代码有加载完成,则使用快商通默认的打开聊天窗口事件,否则使用自定义的打开事件
	if(typeof KS!='undefined'){
		var p = {};
		if(text)p['sText']=text;
		if(openNewChatWin)p['oTarget']='_blank';
		try{
			if(typeof KS.openChatWin=='function'){
				KS.openChatWin(p);
			}else if(typeof KS.openChatLink=='function'){
				KS.openChatLink(p);
			}else{
				ksOpenLink();
			}
		}catch(e){
			ksOpenLink();
		}
	}else{
		ksOpenLink();
	}
};

$(function(){
    $('body').on('click', '.kefu_btn', function (e) {
        var option = "height=100, width=400, toolbar =no, menubar=no, scrollbars=no, resizable=no, location=no, status=no"
        //window.open("http://kf7.kuaishang.cn/bs/im/66510/56293/998837.htm", "newwindow") 
        onKST();
	    return false;
    });
});