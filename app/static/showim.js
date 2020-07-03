function showImage(fileInput) {
        var files = fileInput.files;
        for (var i = 0; i < files.length; i++) {           
            var file = files[i];
            var imageType = /image.*/;     
            if (!file.type.match(imageType)) {
                continue;
            }           
            var img=document.getElementById("pic"); //метод возвращает ссылку на элемент, коорый имеет атрибут id с указанным знач           
            var img0=document.getElementById("pic0");

            img.file = file;
            img0.file = file;
    
            var reader = new FileReader();
            reader.onload = (function(Img1) { //событие onload используется как указатель, что веб страница полностью загружена
                return function(e) { 
                    Img1.src = e.target.result; //триггер target,позволяющий получить доступ к элементу, над которым произошло событие
                }; 
            })(img);


            var reader0 = new FileReader();
            reader0.onload = (function(Img1) { //событие onload исполь$
                return function(e) {
                    Img1.src = e.target.result; //триггер target,позв$
                };
            })(img0);



            reader.readAsDataURL(file); //метод readAsDataURL используется для чтения содержимого указанного file
            reader0.readAsDataURL(file); 
        }
    
    }
