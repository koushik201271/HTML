document.addEventListener("DOMContentLoaded", () => {
    const timeDisplay = document.getElementById("timeDisplay");
    const startBtn = document.getElementById("startBtn");
    const pauseBtn = document.getElementById("pauseBtn");
    const resetBtn = document.getElementById("resetBtn");

    let hours = 0, minutes = 0, seconds = 0;
    let timerInterval = null;
    let isRunning = false;

    function updateTime() {
        seconds++;
        if (seconds == 60) {
            seconds = 0;
            minutes++;
        }
        if (minutes == 60) {
            minutes = 0;
            hours++;
        }

        hours = String(hours).padStart(2, "0");
        minutes = String(minutes).padStart(2, "0");
        seconds = String(seconds).padStart(2, "0");
         timeDisplay.textContent = `${hours}:${minutes}:${seconds}`;
    }

    startBtn.addEventListener("click", () =>{
        if (!isRunning) {
            timerInterval = setInterval(updateTime, 1000);
            isRunning = true;
        }
    });

    pauseBtn.addEventListener("click", () =>{
        clearInterval(timerInterval);
        isRunning = false;
    });

    resetBtn.addEventListener("click", () =>{
        clearInterval(timerInterval);
        isRunning = false;
        hours = 0;
        minutes = 0;
        seconds = 0;
        timeDisplay.textContent = "00:00:00";
    });
});