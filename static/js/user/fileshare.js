   function validateFileSize(input) {
      const maxSize = 1024 * 1024 * 1024; // 1 GB in bytes
      if (input.files && input.files[0].size > maxSize) {
        alert("File size exceeds the maximum limit of 1 GB.");
        input.value = ''; // Clear the file input
      }
    }

    
