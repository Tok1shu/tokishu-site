// Progressive enhancement only: all content is already in the HTML.
(function(){
  try{
    var cards=document.querySelectorAll('.card,.link');
    cards.forEach(function(c){c.addEventListener('pointermove',function(ev){var r=c.getBoundingClientRect();c.style.setProperty('--mx',(ev.clientX-r.left)+'px');c.style.setProperty('--my',(ev.clientY-r.top)+'px');});});
    if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
    var items=document.querySelectorAll('section:not(.hero),.hcopy,.ava');
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.05});
    items.forEach(function(el){io.observe(el);});
    document.documentElement.classList.add('js');
    setTimeout(function(){items.forEach(function(el){el.classList.add('in');});},2500);
  }catch(e){document.documentElement.classList.remove('js');}
})();
