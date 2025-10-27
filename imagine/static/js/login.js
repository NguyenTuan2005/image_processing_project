
document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.querySelector("input[placeholder='Tên đăng nhập']").value;
    const password = document.querySelector("input[placeholder='Mật khẩu']").value;

    if (username === "admin" && password === "123456") {
        localStorage.setItem("isLoggedIn", "true");
        localStorage.setItem("email", "admin@gmail.com");

        window.location.href = "home.html"; // Chuyển về trang Home
    } else {
        alert("Sai thông tin đăng nhập");
    }
});
