function updateDateTime() {
            const datetimeElement = document.getElementById("datetime");
            const now = new Date();
            const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            const timeOptions = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
            const formattedDate = now.toLocaleDateString(undefined, dateOptions);
            const formattedTime = now.toLocaleTimeString(undefined, timeOptions);
            datetimeElement.textContent = `${formattedDate}, ${formattedTime}`;
        }

        // Update date and time initially and then every second
        updateDateTime();
        setInterval(updateDateTime, 1000);