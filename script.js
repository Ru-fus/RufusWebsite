document.addEventListener('DOMContentLoaded', function () {
    const hiddenElements = document.querySelectorAll('.hidden');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                entry.target.classList.remove("hidden");
            }
        });
    });

    hiddenElements.forEach((element) => observer.observe(element));
});

const countdown = () => {
    const countDate = new Date("Dec 2, 2025 00:00:00").getTime();
    const now = new Date().getTime();
    const gap = countDate - now;

    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    const textDay = Math.floor(gap / day);
    const textHour = Math.floor((gap % day) / hour);
    const textMinute = Math.floor((gap % day % hour) / minute);
    const textSecond = Math.floor((gap % day % hour % minute) / second);

    document.querySelector("#days").innerText = textDay;
    document.querySelector("#hours").innerText = textHour;
    document.querySelector("#minutes").innerText = textMinute;
    document.querySelector("#seconds").innerText = textSecond;
};

setInterval(countdown, 1000);
