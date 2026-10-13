// Инициализация карты Leaflet на странице контактов
document.addEventListener("DOMContentLoaded", function () {
    const mapElement = document.getElementById("map");

    // Если карты на странице нет — выходим
    if (!mapElement) return;

    // Читаем координаты из data-атрибутов
    const lat = parseFloat(mapElement.dataset.lat) || 42.8746;
    const lng = parseFloat(mapElement.dataset.lng) || 74.5698;
    const title = mapElement.dataset.title || "Мы здесь!";
    const address = mapElement.dataset.address || "";

    // Создаём карту
    const map = L.map("map").setView([lat, lng], 15);

    // Подключаем слой OpenStreetMap (бесплатно, без API-ключа)
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "&copy; OpenStreetMap contributors",
        maxZoom: 19,
    }).addTo(map);

    // Добавляем маркер
    const marker = L.marker([lat, lng]).addTo(map);

    // Всплывающая подсказка
    marker
        .bindPopup(`<strong>${title}</strong><br>${address}`)
        .openPopup();
});