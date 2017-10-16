$(document).ready(function() {
  $('.likes').click(function(){
    var sched_id;
    var curruser;
    sched_id = $(this).attr("data-scheduleid");
    curruser_id = $(this).attr("data-user");
    $.get('/profiles/like_schedule/', {schedule_id: sched_id, current_user: curruser_id}, function(data){
      $('#' + sched_id).html(data);
//      if (data.liked) {
  //      $('.' + sched_id).attr('src', '/img/liked2')
    //  } else {
      //  $('.' + sched_id).attr('src', '/img/notliked2')
    //  }
    });
  });
});
