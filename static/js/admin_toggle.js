document.addEventListener('DOMContentLoaded', function() {
    // Logic to grey out fields in the TabularInline
    const toggleFields = (row) => {
        const imgInput = row.querySelector('.field-image input');
        const videoInput = row.querySelector('.field-video_url input');
        
        if (!imgInput || !videoInput) return;

        const updateStates = () => {
            if (videoInput.value.trim() !== "") {
                imgInput.style.opacity = "0.3";
                imgInput.style.pointerEvents = "none";
            } else if (imgInput.files && imgInput.files.length > 0) {
                videoInput.style.opacity = "0.3";
                videoInput.style.pointerEvents = "none";
            } else {
                imgInput.style.opacity = "1";
                imgInput.style.pointerEvents = "auto";
                videoInput.style.opacity = "1";
                videoInput.style.pointerEvents = "auto";
            }
        };

        videoInput.addEventListener('input', updateStates);
        imgInput.addEventListener('change', updateStates);
        updateStates();
    };

    // Watch for existing rows and new rows added via "Add another"
    document.querySelectorAll('.inline-related tr').forEach(toggleFields);
    
    // Django admin hook for new rows
    $(document).on('formset:added', function(event, $row, formsetName) {
        toggleFields($row[0]);
    });
});
