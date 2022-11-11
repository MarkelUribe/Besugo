(function ($) {
  "use strict";

    $(document).ready(function () {

      let json = {id:1, cont:0, funtz:'hasi'};
      let csrftoken = "{{csrf_token}}";
      $.ajax({
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        url:  "/updatecarro/",
        data: json,
        dataType: 'json',
        success: function (data) {
          //prezio totala jarri
          $("#preziototala").html("TOTALA: "+data[0].total.toFixed(2)+"€")
          //aukeratutako produktuen kopurua jarri
          for (let i = 0; i < data[0].eskaerak.length; i++) {
            $("#contador"+data[0].eskaerak[i].produktuaid).val(data[0].eskaerak[i].kopurua)
          }
          console.log(data)
        }, error: function(e){
          alert("errorea: " + e);
          console.log(e);
        }
      });

      function ajaxkarritoupdate(id, funtzio){
        let contador = "#contador" + id;
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
            //prezio totala jarri
            $("#preziototala").html("TOTALA: "+data[0].total.toFixed(2)+"€")
            //aukeratutako produktuen kopurua jarri
            for (let i = 0; i < data[0].eskaerak.length; i++) {
              $("#contador"+data[0].eskaerak[i].produktuaid).val(data[0].eskaerak[i].kopurua)
            }
            console.log(data)
          }, error: function(e){
            alert("errorea: " + e);
            console.log(e);
          }
        });
      }

        $(".gehiMariskada").click(function(e){
            e.preventDefault();

            var id = $(this).val(); 
            let contador = "#contador" + id;
            let balio = parseInt($(contador).val()) + 1;
            $(contador).val(balio);
            ajaxkarritoupdate(id, 'gei');
        });

        $(".kenMariskada").click(function(e){
            e.preventDefault();

            var id = $(this).val(); 
            //alert(id);
            let contador = "#contador" + id;
            let balio = parseInt($(contador).val()) - 1;
            if(balio<0){balio=0}
            $(contador).val(balio);
            ajaxkarritoupdate(id, 'ken');

        });
    
        $(".contador").on("input", function(){
            var id = $(this).attr('id');
            id = id.split("r").pop();
            ajaxkarritoupdate(id, 'ken');
        });



    });
})(jQuery);