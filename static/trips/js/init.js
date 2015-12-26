(function($){
  $(function(){

    $('.button-collapse').sideNav({
      menuWidth: 300, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });

    $('.parallax').parallax();
    $('select').material_select();

    var options = [
    {selector: '#staggered-test', offset: 10, callback: 'Materialize.showStaggeredList("#staggered-test")' },
    {selector: '#image-test', offset: 500, callback: 'Materialize.fadeInImage("#image-test")' } ];

    Materialize.scrollFire(options);

  }); // end of document ready
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 80 // Creates a dropdown of 15 years to control year

  });
  $(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
    $('.tooltipped').tooltip({delay: 50});


  });
})(jQuery); // end of jQuery name space
