
export async function hello() {
    const response = await fetch("http://127.0.0.1:8000/hello/");
    const data = await response.text();
    return data;
}