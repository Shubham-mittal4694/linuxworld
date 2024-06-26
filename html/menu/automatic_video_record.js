let stream;
let mediaRecorder;
let chunks = [];

const startRecording = () => {
  navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(function (userMediaStream) {
      stream = userMediaStream;
      const recordedVideo = document.getElementById('recordedVideo');
      recordedVideo.srcObject = stream;
      recordedVideo.play();

      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.ondataavailable = function (e) {
        chunks.push(e.data);
      };

      mediaRecorder.onstop = function () {
        const blob = new Blob(chunks, { 'type': 'video/mp4' });
        chunks = [];
        const videoUrl = URL.createObjectURL(blob);
        const downloadLink = document.getElementById('downloadLink');
        downloadLink.href = videoUrl;
        downloadLink.download = 'recorded-video.mp4';
        downloadLink.style.display = 'block';
      };

      mediaRecorder.start();
    })
    .catch(function (err) {
      console.error('Error accessing media devices: ', err);
    });
};

const stopRecording = () => {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop();
    stream.getTracks().forEach(track => track.stop());
  }
};

document.getElementById('startRecording').addEventListener('click', startRecording);
document.getElementById('stopRecording').addEventListener('click', stopRecording);
