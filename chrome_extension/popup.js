document.addEventListener('DOMContentLoaded', function() {
    const inputValue = document.getElementById('inputValue');
    const saveBtn = document.getElementById('saveBtn');
    const retrieveBtn = document.getElementById('retrieveBtn');
    const status = document.getElementById('status');

    // Save the value to chrome.storage
    saveBtn.addEventListener('click', function() {
        const value = inputValue.value;
        chrome.storage.sync.set({ 'storedValue': value }, function() {
            status.textContent = 'Value saved!';
        });
    });

    // Retrieve the value from chrome.storage
    retrieveBtn.addEventListener('click', function() {
        chrome.storage.sync.get(['storedValue'], function(result) {
            if (result.storedValue) {
                status.textContent = 'Retrieved value: ' + result.storedValue;
            } else {
                status.textContent = 'No value stored!';
            }
        });
    });
});

