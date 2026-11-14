(function(){
  var nav=document.querySelector('.snav');if(!nav)return;
  var b=nav.querySelector('.burger');
  if(b)b.addEventListener('click',function(){var on=nav.classList.toggle('on');b.setAttribute('aria-expanded',on?'true':'false')});
  nav.querySelectorAll('.menu>li>button').forEach(function(btn){
    btn.addEventListener('click',function(e){
      var li=btn.parentNode,open=li.classList.contains('open');
      nav.querySelectorAll('.menu>li.open').forEach(function(x){x.classList.remove('open')});
      if(!open)li.classList.add('open');
      btn.setAttribute('aria-expanded',!open?'true':'false');e.stopPropagation();
    });
  });
  document.addEventListener('click',function(e){if(!nav.contains(e.target)){nav.querySelectorAll('.menu>li.open').forEach(function(x){x.classList.remove('open')})}});
  nav.querySelectorAll('.menu a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('on')})});
})();
