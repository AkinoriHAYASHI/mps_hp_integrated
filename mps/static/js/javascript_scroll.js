            $(function() {
                $('#gallery').smoothDivScroll({
                    mousewheelScrolling: "allDirections",
                    manualContinuousScrolling: true,
                    autoScrollingMode: "onStart"
                });
                $('#gallery').bind("mouseout", function() {
                    $('#gallery').smoothDivScroll("startAutoScrolling");
                });
            });