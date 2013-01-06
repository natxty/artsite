/*!
 * Artsite Scripts : 12/12/2012 :-)
 * Nathaniel Clark :: @natxty
 * Content Slider/Animations Inspired by a prototype by Colin Kahn :: @colinkahn
 * Document dimensions taken from Ryan Griffin: @therg
 */

var ArtSite = (function () {
    var self = {},
    debug = true,
    $e = {},
    $win = $(window),
    $doc = $(document),
    $body = $('body'),

    docHeight,
    docWidth,

    obotURL = '/obot/response/';


    /* ============================================================================== */
    /* Helper functions
    /* ============================================================================== */
    function _log(str) {
        if(debug) console.log(str);
    }

    //Grab the height of the entire document correctly
    function _get_document_height(){
        var body = document.body,
            html = document.documentElement;
        return Math.max( body.scrollHeight, body.offsetHeight,
                               html.clientHeight, html.scrollHeight, html.offsetHeight );
    }

    function _get_document_width() {
        return $doc.width();
    }

    // Set the hight of param:JQobject to document height
    function reset_height($object) {
        $object.css({height: _get_document_height()+'px'});
    }

    //To-do: Generic recalc function to fit images in browser dimensions properly



    /* ============================================================================== */
    /* Main AJAX functions
    /* ============================================================================== */


    /* ============================================================================== */
    /* Image Overlayer Link Fade In Functions
    /* ============================================================================== */



    /* ============================================================================== */
    /* initialization
    /* ============================================================================== */
    self.init = function () {

        //start chat?
        var box = null;
          $("a.chatlaunch").click(function(event, ui) {
            event.preventDefault();

              if(box) {
                  box.chatbox("option", "boxManager").toggleBox();
              }
              else {
                  box = $("#chat_div").chatbox({
                    id:"you", 
                    user:{key : "value"},
                    title : "john.o.bot",
                    messageSent : function(id, user, msg) {
                        //if we need to log:
                        //$("#log").append(id + " said: " + msg + "<br/>");

                        //post users':
                        $("#chat_div").chatbox("option", "boxManager").addMsg(id, msg);

                        //pause a random ##:
                        randWait = Math.floor(Math.random()*1001) + 500;

                        window.setTimeout(function () {
                          //get response && post:
                            $.get(obotURL, function(data) {
                                $("#chat_div").chatbox("option", "boxManager").addMsg('johno', data);
                            });
                        },randWait);

                        


                    }});
              }
          });

        //check document dimensions
        self.docHeight = _get_document_height();
        self.docWidth = _get_document_width();

        //initial check:
        //console.log('height: ' + self.docHeight + ', width: ' + self.docWidth);
        
        //rework if resized:
        $(window).resize(function(e){
            self.docHeight = _get_document_height();
            self.docWidth = _get_document_width();

            //console.log('height: ' + self.docHeight + ', width: ' + self.docWidth);
            
        })
        
        /* Content Animations */

        $('.hp-item').click(function(e) {

            e.preventDefault();

            var c=0,
                _this = this;

            $('.hp-item').each(function(i,el) {
                if (el==_this) {

                    var setHeight = (self.docHeight * 0.8)

                    var cssObj = {
                      'height': setHeight,
                    }

                    /* size image correctly */
                    var ximg = $(el).find('.contentArea .side_a img').css( cssObj )
                    //console.log(ximg)

                    /* Add area // Fade in */
                    $(el).addClass('active')
                    $(el).find('.contentArea')
                        .clone()
                        .appendTo('body')
                        .fadeIn('slow')
                } else {
                    /*
                    setTimeout(function() {
                        $(el).addClass('offscreen')
                    }, 50*c);
                    c++
                    */
                }
            })

            $('.close').removeClass('hide')
        })

        $('.close').live('click',function() {
            $('body > .contentArea').fadeOut('slow', function() {
                $(this).remove()
            })
            var c=0,
                active = $('.hp-item.active').get(0)
            $('.hp-item').each(function(i,el) {
                if (el == active) {
                    $(el).removeClass('active')
                } else {
                    /*
                    setTimeout(function() {
                        $(el).removeClass('offscreen')
                    }, 50*c);
                    c++
                    */
                }
            })
            $('.close').addClass('hide')
            return false
        })
        
    }

    return self;
}());