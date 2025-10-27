document
        .getElementById("registerForm")
        .addEventListener("submit", function (e) {
          const form = this;
          const password = document.getElementById("password");
          const confirmPassword = document.getElementById("confirmPassword");

          confirmPassword.setCustomValidity("");

          if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity("Mật khẩu không khớp");
          }

          if (!form.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
          } else {
            e.preventDefault();
            alert(" Đăng ký thành công!");
            form.reset();
          }

          form.classList.add("was-validated");
        });
      // Toggle hiển thị mật khẩu
      function togglePassword(inputId, toggleIconId) {
        const input = document.getElementById(inputId);
        const icon = document.getElementById(toggleIconId);

        icon.addEventListener("click", () => {
          const isPassword = input.type === "password";
          input.type = isPassword ? "text" : "password";
          icon.classList.toggle("fa-eye");
          icon.classList.toggle("fa-eye-slash");
        });
      }

      togglePassword("password", "togglePassword");
      togglePassword("confirmPassword", "toggleConfirm");