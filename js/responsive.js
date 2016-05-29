$(document).ready(function() {
  var width = $(window).width(); //Get width of browser window

  //Phones
  if(width <= 450) {
   function navElement(id, imgDir) { //Create temporary element object
     this.id = id;
     this.imgDir = imgDir;
   }

   var navElems = [ //Element array
     new navElement("#home", "/website/imgs/home.png"),
     new navElement("#videos", "/website/imgs/videos.png"),
     new navElement("#pictures", "/website/imgs/pictures.png"),
     new navElement("#upload", "/website/imgs/upload.png"),
     new navElement("#about", "/website/imgs/about.png")
   ];

   for(var i = 0; i < navElems.length; i++) { //Loops through all elements
     var elem = navElems[i]; //Get nav element object
     var jElem = $(navElems[i].id); //Select an element with jQuery based on the ID

     if(jElem.get(0).nodeName == "LI") { //Makes sure elements are on the nav bar
       var text = jElem.text();
       var html = jElem.html();

       html = html.replace(text, "<img src='" + elem.imgDir + "' />");

       jElem.html(html);
     }
   }
  }
});
