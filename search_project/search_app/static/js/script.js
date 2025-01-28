document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.getElementById("menuToggle");
    const searchForm = document.getElementById("searchForm");

    // ハンバーガーメニュークリック時のイベントリスナー
    menuToggle.addEventListener("click", () => {
        console.log("ハンバーガーメニューがクリックされました"); // デバッグ用
        searchForm.classList.toggle("hidden"); // hiddenクラスをトグル
        console.log(searchForm.classList);
    });
});

    document.addEventListener('DOMContentLoaded', () => {
        const images = document.querySelectorAll('.slideshow-image'); // 全ての画像を取得
        let currentIndex = 0;

        setInterval(() => {
            // 現在の画像を非表示
            images[currentIndex].style.display = 'none';

            // 次の画像を表示（最後の画像の次は最初に戻る）
            currentIndex = (currentIndex + 1) % images.length;
            images[currentIndex].style.display = 'block';
        }, 5000); // 5秒ごとに切り替え
    });

