function startJarvis() {
  eel.start_jarvis();
  document.getElementById("status").innerText = "Jarvis is listening...";
}

function stopJarvis() {
  eel.stopJarvis();
  document.getElementById("status").innerText = "Jarvis has stopped.";
}
eel.expose(update_status);
function update_status(status) {
    document.getElementById("status").innerText = status;
}