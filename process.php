<?php
// التحقق من إرسال النموذج
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // استلام البيانات من النموذج
    $name = $_POST['name'];
    $email = $_POST['email'];
    $age = $_POST['age'];

    try {
        // الاتصال بقاعدة البيانات SQLite
        $pdo = new PDO("sqlite:my_database.db");

        // إنشاء الجدول إذا لم يكن موجودًا
        $pdo->exec("CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )");

        // إضافة البيانات
        $stmt = $pdo->prepare("INSERT INTO users (name, email, age) VALUES (:name, :email, :age)");
        $stmt->execute([
            ':name' => $name,
            ':email' => $email,
            ':age' => $age
        ]);

        echo "Data added successfully!";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
} else {
    echo "Invalid Request!";
}
?>
