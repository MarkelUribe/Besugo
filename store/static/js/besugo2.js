(function ($) {
  "use strict";
  
  $(document).ready(function () {
    function totaljaso(){
      let json = {};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/totalajaso/",
        data: json,
        dataType: 'json',
        success: function (data) {
          //alert(data[0].mezua);
          $("#total").html(data[0].total+"€");
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });

    }
    totaljaso();

    function ajaxkarritoupdate(id, funtzio){
      let contador = "#cont" + id;
      let contval=$(contador).val();
      let json = {id:id, cont:contval, funtz:funtzio};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/updatecarro/",
        data: json,
        dataType: 'json',
        success: function (data) {
          $("#total").html(data[0].total.toFixed(2)+"€");
          //aukeratutako produktuen kopurua jarri
          
          for (let i = 0; i < data[0].eskaerak.length; i++) {
            $("#contador"+data[0].eskaerak[i].produktuaid).val(data[0].eskaerak[i].kopurua)
          }
          if(data[0].mezua == "Ez dago stock-ik"){
            alert(data[0].mezua);
            $(contador).val(data[0].stock)
          }
          console.log(data)
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });
    }


    $(".gehiMariskada").click(function (e) {
      e.preventDefault();
      var id = $(this).val();
      let contador = "#cont" + id;
      let balio = parseInt($(contador).val()) + 1;
      $(contador).val(balio);
      ajaxkarritoupdate(id, 'gei');
      //totaljaso();

    });

    $(".kenMariskada").click(function (e) {
      e.preventDefault();

      var id = $(this).val();
      //alert(id);
      let contador = "#cont" + id;
      let balio = parseInt($(contador).val()) - 1;
      if (balio < 0) {
        balio = 0;
      }
      $(contador).val(balio);
      ajaxkarritoupdate(id, 'ken');
      //totaljaso();
    });


    $(".basura").click(function (e) {
      var id = $(this).attr('id');
      id = id.split("ra").pop();


      let json = {id:id};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/eskaeraezabatu/",
        data: json,
        dataType: 'json',
        success: function (data) {
          totaljaso();
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });

      $(this).parent().parent().remove();
      
    });

    $(".contador").on("input", function(){
      var id = $(this).attr('id');
      id = id.split("t").pop();
      ajaxkarritoupdate(id, 'ken');
      //totaljaso();
  });

  $("#btnComprar").click(function (e) {
      let json = {};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/ordainketaegin/",
        data: json,
        dataType: 'json',
        success: function (data) {
          if (data[0].mez !== ""){
            alert(data[0].mez);
          }else{
            pdf(data);
            window.location.href = '/index';
          }
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });
  });



  });

  function pdf(data){
    if (confirm('Eskaera egin da!, Faktura gorde nahi duzu?')) {
      var doc = new jsPDF();
      let text = "";
      text += 'Faktura '+data[0].eguna +" \r\n ";
      text += data[0].izena +" \r\n \r\n ";
      for (let i = 0; i < data[0].lista.length; i++) {
        text += data[0].lista[i].produktua + " | Unitateak: " + data[0].lista[i].kopurua + " | " + data[0].lista[i].prezioa+"€ \r\n ";
      }
      text += '\r\n Guztira: '+data[0].total+"€";
      console.log(text);
      doc.text(text, 10, 10);
      doc.save('faktura'+data[0].eguna+'.pdf');
    }
    
  }
 
})(jQuery);
