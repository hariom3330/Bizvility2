function dropdown(){
    document.getElementById("dropdown").classList.toggle("show");
}
window.onclick=function(event){
    if(!event.target.matches('.dropbtn')){
        var dropdowns=document.getElementsByClassName('dropdown-content');
        var i;
        for(i=0;i<dropdowns.length;i++){
            var opendropdown = dropdowns[i];
            if(opendropdown.classList.contains('show'))
            {
                opendropdown.classList.remove('show');
            }
        }
    }
}
function dropdownfilter(){
    document.getElementById("dropdownfilter").classList.toggle("showfilter");
}
window.onclick=function(event){
    if(!event.target.matches('.dropbtnfilter')){
        var dropdowns=document.getElementsByClassName('dropdown-content-filter');
        var i;
        for(i=0;i<dropdowns.length;i++){
            var opendropdown = dropdowns[i];
            if(opendropdown.classList.contains('show'))
            {
                opendropdown.classList.remove('show');
            }
        }
    }
}