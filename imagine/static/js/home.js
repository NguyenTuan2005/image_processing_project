function goLogin() {
    window.location.href = "login.html";
}

// Kiểm tra trạng thái đăng nhập
document.addEventListener("DOMContentLoaded", () => {
    const isLoggedIn = localStorage.getItem("isLoggedIn");
    const email = localStorage.getItem("email");

    if (isLoggedIn === "true" && email) {
        document.getElementById("loginBtn").style.display = "none";
        document.getElementById("loggedInfo").style.display = "block";
        document.getElementById("userEmail").innerText = email;
    } else {
        document.getElementById("loginBtn").style.display = "block";
        document.getElementById("loggedInfo").style.display = "none";
    }
});

// Đăng xuất từ modal
function logout() {
    localStorage.clear();
    location.reload();
}