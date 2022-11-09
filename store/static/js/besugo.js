(function ($) {
  "use strict";

    $(document).ready(function () {
        $(".gehiMariskada").click(function(e){
            e.preventDefault();

            var id = $(this).val(); 
            //alert(id);
            let contador = "#contador" + id;
            let balio = parseInt($(contador).val()) + 1;
            $(contador).val(balio);
            let contval=$(contador).val();

            let json = {id:id, cont:contval,};
            let csrftoken = "{{csrf_token}}";
            $.ajax({
              type: 'POST',
              headers: { 'X-CSRFToken': csrftoken },
              url:  "/updatecarro/",
              data: json,
              dataType: 'json',
              success: function (data) {
                $("#preziototala").html("TOTALA: "+data[0].total.toFixed(2)+"€")
                alert(data[0].mezua)
                console.log(data[0].eskaerak)
              }, error: function(e){
                alert("errorea: " + e);
                console.log(e);
              }
            });

        });

        $(".kenMariskada").click(function(e){
            e.preventDefault();

            var id = $(this).val(); 
            //alert(id);
            let contador = "#contador" + id;
            let balio = parseInt($(contador).val()) - 1;
            if(balio<0){balio=0}
            $(contador).val(balio);
        });
    




    });
})(jQuery);