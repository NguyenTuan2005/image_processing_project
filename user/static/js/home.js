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

async function generate() {
    const prompt = document.getElementById("prompt-input").value;
    const result = document.getElementById("result");

    if (!prompt.trim()) {
        result.textContent = "Vui lòng nhập mô tả trước khi tạo ảnh.";
        return;
    }

    result.textContent = "Đang tạo hình ảnh...";

    try {

        const response = await fetch("/generate/", {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({ prompt })
        });

        if (!response.ok) {
            throw new Error("Lỗi khi tạo ảnh");
        }

        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);

        result.innerHTML = `<img src="${imageUrl}" alt="Kết quả tạo ảnh" class="img-fluid rounded shadow" style="max-height: 80px" />`;
    } catch (error) {
        result.textContent = "Đã xảy ra lỗi khi tạo ảnh.";
    }
}

// Helper to get CSRF token
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}