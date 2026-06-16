# Space Invader × Git/GitHub 三小時教程

給**剛要上大一的你**:用做遊戲的方式,把 GitHub 的協作流程練到熟。
重點不是遊戲多厲害,而是你會反覆操作同一套流程三次 —— 第三次你就不用看講義了。

## 你會學到的核心循環

每做一個遊戲功能,就完整跑一次這個循環:

```
開 Issue → 開 branch → 改程式 → commit → push → 開 PR → merge → 切回 main → pull
```

> 👩‍🏫 教學者請參考 [teaching-plan.md](teaching-plan.md):設計理念、帶課節奏與給新手的提醒。

## 名詞白話翻譯

| 指令 / 名詞 | 白話 |
|------------|------|
| `commit` | 拍一張存檔快照,寫一句「我改了什麼」 |
| `branch`(分支) | 開一條平行的草稿線,不影響正式版 |
| `push` | 把本機的 commit 上傳到 GitHub |
| `pull` | 把 GitHub 上的最新版抓回本機 |
| Pull Request (PR) | 「請把我這條分支的修改併進正式版」的申請單 |
| `merge`(合併) | 真的把分支併進去 |
| conflict(衝突) | 兩個人改了同一行,Git 不知道聽誰的,要你決定 |

## 時間軸(總共三小時)

| 時間 | 階段 | 遊戲功能 | Git 重點 |
|------|------|----------|----------|
| 0:00–0:30 | 暖身 | 跑起遊戲、讀懂程式 | clone / status / log,認識 main |
| 0:30–1:15 | [階段一](stage1-lives.md) | 玩家三條命 | 完整跑第一次循環 + 第一個 PR |
| 1:15–2:00 | [階段二](stage2-levels.md) | 關卡系統 | 用 Issue 追蹤 + 好的 commit |
| 2:00–2:50 | [階段三](stage3-bunkers.md) | 防護罩 + 爆炸特效 | **解決 merge 衝突** + `.gitignore` |
| 2:50–3:00 | 收尾 | 玩成果 | 回顧 commit 歷史與貢獻圖 |

## 環境準備(課前)

```bash
# 1. 安裝 Python(3.8 以上)與 Git,略
# 2. 安裝遊戲套件
python -m pip install pygame

# 3. 把這個 repo 抓下來
git clone <你的 repo 網址>
cd vibe-coding

# 4. 確認遊戲跑得起來(按關閉視窗即可結束)
python space_invader.py
```

## 檔案說明

- `space_invader.py` —— 起點程式碼(階段一就從這份開始改)
- `solutions/stage1_lives.py` —— 階段一解答
- `solutions/stage2_levels.py` —— 階段二解答
- `solutions/stage3_bunkers.py` —— 階段三解答
- [templates.md](templates.md) —— Issue / PR 可以直接複製的範本

> 卡關時再看解答,先自己試。對照解答時,在編輯器裡用「比較檔案」功能看差異最有感。

## 操作方式

- `←` `→`:移動太空船
- `空白鍵`:發射
- `R`:遊戲結束後重新開始
