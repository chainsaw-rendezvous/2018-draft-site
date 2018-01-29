/**
*
* -------------------------------------------------
*
* Template : Asap - A Onepage Corporate Template
* Author : thecodrops
* Author URI : http://thecodrops.com
*
* --------------------------------------------------
*
**/

/*
(function ($) {
    'use strict';
    jQuery(document).ready(function () {

    });
})(jQuery);
*/


/* Attach events after the button has been loaded */
window.addeventasync = function(){

    /* Capture click on button */
    addeventatc.register('button-click', function(obj){

        /* Log */
        console.log('button-click -> ' + obj.id);

    });

    /* Capture mouseover on button */
    addeventatc.register('button-mouseover', function(obj){

        /* Log */
        console.log('button-mouseover -> ' + obj.id);

    });

    /* Capture mouseout on button */
    addeventatc.register('button-mouseout', function(obj){

        /* Log */
        console.log('button-mouseout -> ' + obj.id);

    });

    /* Capture when dropdown is being displayed */
    addeventatc.register('button-dropdown-show', function(obj){

        /* Log */
        console.log('button-dropdown-show -> ' + obj.id);

    });

    /* Capture when dropdown is being hidden */
    addeventatc.register('button-dropdown-hide', function(obj){

        /* Log */
        console.log('button-dropdown-hide -> ' + obj.id);

    });

    /* Capture when an option in the dropdown is clicked */
    addeventatc.register('button-dropdown-click', function(obj){

        /* Log */
        console.log('button-dropdown-click -> ' + obj.id + ', service -> ' + obj.service);

        /* Track event click with e.g. Google Analytics (using analytics.js)
        https://developers.google.com/analytics/devguides/collection/analyticsjs/events */
        //ga('send', 'event', 'AddEvent.com Button', 'button-dropdown-click -> ' + obj.id + ', service -> ' + obj.service, '2018 Rendezvous');

    });

};