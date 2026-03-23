from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Kho từ vựng mẫu (bạn có thể thêm thoải mái)
vocabulary = {
    "Test 1": [
        {"english": "extensive", "vietnamese": "sâu rộng, bao quát", "explanation": "Mô tả cái gì đó có phạm vi lớn, chi tiết và toàn diện."},
        {"english": "resilient", "vietnamese": "kiên cường", "explanation": "Có khả năng phục hồi nhanh chóng sau khó khăn."},
        {"english": "ubiquitous", "vietnamese": "phổ biến khắp nơi", "explanation": "Có mặt ở mọi nơi, rất phổ biến."},
        {"english": "ephemeral", "vietnamese": "ngắn ngủi, thoáng qua", "explanation": "Tồn tại trong thời gian rất ngắn."},
        {"english": "meticulous", "vietnamese": "cẩn thận, tỉ mỉ", "explanation": "Chú ý đến từng chi tiết nhỏ nhất."},
        {"english": "serendipity", "vietnamese": "may mắn tình cờ", "explanation": "Khám phá điều tốt đẹp một cách bất ngờ."},
        {"english": "quintessential", "vietnamese": "điển hình, bản chất", "explanation": "Đại diện hoàn hảo cho một đặc tính."},
        {"english": "plethora", "vietnamese": "rất nhiều, dư thừa", "explanation": "Số lượng lớn đến mức thừa thãi."},
        {"english": "innovative", "vietnamese": "đổi mới, sáng tạo", "explanation": "Mang lại ý tưởng mới mẻ và cải tiến."},
        {"english": "pragmatic", "vietnamese": "thực tế", "explanation": "Tập trung vào giải pháp thực tế thay vì lý thuyết."}
        ],
    "Test 2": [
        {"english": "allocate", "vietnamese": "phân bổ", "explanation": "To distribute for a purpose."},
        # ... thêm từ cho Test 2
    ],
    # ... tiếp tục đến Test 10
    # Ví dụ tổng cộng khoảng 1000-1500 từ TOEIC phổ biến
}

@app.route('/')
def index():
    # Chuyển dữ liệu sang JSON để JS sử dụng
    return render_template('index.html', vocabulary=json.dumps(vocabulary))
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)