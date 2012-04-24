var CSSrules = {
    'textarea' : function(element){
            element.onkeydown = function(event){
                return doKeyPress(element,event);
            }
            ,
            element.onpaste = function(){
                return doPaste(element);
            }
            ,
            element.onkeyup = function(){
                return doKeyUp(element);
            }
            ,
            element.onblur = function(){
                return doKeyUp(element);
            }
    }
}

Behaviour.register(CSSrules);

var detect = navigator.userAgent.toLowerCase();

// Keep user from entering more than maxLength characters
function doKeyPress(obj,evt){
    maxLength = obj.getAttribute("maxlength");
    var e = window.event ? event.keyCode : evt.which;
    if ( (e == 32) || (e == 13) || (e > 47)) { //IE
        if(maxLength && (obj.value.length > maxLength-1)) {
            if (window.event) {
                window.event.returnValue = null;
            } else {
                evt.cancelDefault;
                return false;
            }
        }
    }
}
function doKeyUp(obj){
    maxLength = obj.getAttribute("maxlength");
     if(maxLength && obj.value.length > maxLength){
           obj.value = obj.value.substr(0,maxLength);
     }
    sr = obj.getAttribute("showremain");
    if (sr) {
        document.getElementById(sr).innerHTML = maxLength-obj.value.length;
    }
}

// Cancel default behavior and create a new paste routine
function doPaste(obj){
maxLength = obj.getAttribute("maxlength");
     if(maxLength){
        if ((window.event) && (detect.indexOf("safari") + 1 == 0)) { //IE
          var oTR = obj.document.selection.createRange();
          var iInsertLength = maxLength - obj.value.length + oTR.text.length;
          try {
          var sData = window.clipboardData.getData("Text").substr(0,iInsertLength);
          oTR.text = sData;
          }
          catch (err) {
          }
          if (window.event) { //IE
            window.event.returnValue = null;
     } else {
            //not IE
            obj.value = obj.value.substr(0,maxLength);
            return false;
        }
        }
     }
}
