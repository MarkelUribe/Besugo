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