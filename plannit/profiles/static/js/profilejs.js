$(document).ready(function() {
  $('.likes').click(function(e){
    var sched_id;
    var curruser;
    sched_id = $(this).attr("data-scheduleid");
    curruser_id = $(this).attr("data-user");
    $.get('/profiles/like_schedule/', {schedule_id: sched_id, current_user: curruser_id}, function(data){
      var first = data.split("/")
      $('#' + sched_id).html(first[0]);
      console.log(first[1])
      //$('#likes').html("<input style = 'width : 4%; height: 4%' type = 'image' id = {{schedule.id}} class = 'likes' data-scheduleid = '{{schedule.id}}' data-user = '{{curruser.person.id}}' src = {% static 'img/" + first[1] + "' %}/>");
      //var src = $('.' + sched_id + "image").attr("src");
      //$('.likes' + sched_id + "image").attr("src", "img/" + first[1]);
      //$('.' + sched_id + "image").attr("src", src.slice(0, src.indexOf('img/')) + 'img/' + first[1]);
      e.preventDefault()
      //var $img = $(this);
      //$.get('/profiles/like_schedule/',{ dummy: (new Date()).getTime(), schedule_id: $img.data("scheduleid"), current_user: $img.data("user") }, function(data) {
          //$img.attr('src','img/' + data.split("/")[1])
      });
    });
  });
});
