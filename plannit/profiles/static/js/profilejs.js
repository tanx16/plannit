$(document).ready(function() {
  $('.likes').click(function(){
    console.log("hi")
    var sched_id;
    sched_id = $(this).attr("data-scheduleid");
    console.log(sched_id)
    $.get('/profiles/like_schedule/', {schedule_id: sched_id}, function(data){
      console.log(data)
      $('#' + sched_id).html(data);
    });
  });
});
