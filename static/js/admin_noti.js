async function replaceCardContent() {
    const announcementInput = document.getElementById('announcementInput');
    const noti = document.getElementById('noti')
    const originalCard = document.querySelector('.notification');
    console.log(announcementInput.value)
    const response = await fetch("/admin/notifications/create", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify(announcementInput.value),
      });
      const result = await response.json();
    if (announcementInput.value.trim() !== '') {
      // Clone the original card
      const newCard = originalCard.cloneNode(true);

      // Update content of the new card
      const notificationContent = newCard.querySelector('.notification-content');
      notificationContent.textContent = announcementInput.value.trim();

      // Insert the new card above the original card
      originalCard.parentNode.insertBefore(newCard, originalCard);

      // Clear the input
      announcementInput.value = '';
    }
  }