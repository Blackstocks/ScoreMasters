const previewBtn = document.getElementById("preview")

$('#preview').on('click', function(){
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      $('#contentBox').get(0).requestFullscreen();
    }
  });