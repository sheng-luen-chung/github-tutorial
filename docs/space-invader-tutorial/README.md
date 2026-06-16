# Space Invader × Git/GitHub 教程(兩堂家教制)

給**剛要上大一的你**:用做遊戲的方式,把 GitHub 的協作流程練到熟。
重點不是遊戲多厲害,而是你會反覆操作同一套流程很多次 —— 練到不用看講義為止。

課程分**兩堂**,每堂是 **3 小時講解 + 2 小時回家自練**。

## 第一次上課前,先讀這兩份

1. [git-background.md](git-background.md) —— Git 是什麼、跟 GitHub 差在哪(完全新手必看)
2. [workflow.md](workflow.md) —— **標準工作流程**,整套教程的主軸

## 你會反覆練習的核心循環

```
先拉、開枝、改存推、開 PR 合、再拉、剪枝
= checkout main → pull → checkout -b → 改 → add → commit → push
  → 開 PR → Merge → checkout main → pull → branch -d
```

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

## 課程地圖

### 📘 第一堂:Git 基礎 + 你的第一個 PR(3h 講解)
投影片:[slides/session1.md](slides/session1.md)

| 內容 | 教材 |
|------|------|
| Git 背景 + 工作流程 | [git-background.md](git-background.md) / [workflow.md](workflow.md) |
| 階段一:玩家三條命 | [stage1-lives.md](stage1-lives.md) |
| 看歷史與差異入門 | [history-and-diff.md](history-and-diff.md) |
| 階段二:關卡系統 | [stage2-levels.md](stage2-levels.md) |

➡️ 回家 2 小時:[作業一](homework/homework1.md)

### 📗 第二堂:進階功能 + 解決衝突(3h 講解)
投影片:[slides/session2.md](slides/session2.md)

| 內容 | 教材 |
|------|------|
| 階段三:防護罩 + 爆炸特效 | [stage3-bunkers.md](stage3-bunkers.md) |
| **衝突處理**(本堂重點) | [stage3-bunkers.md](stage3-bunkers.md) Part C |
| **回到過去的版本**(歷史重現)+ 比差異 | [history-and-diff.md](history-and-diff.md) |
| `.gitignore` + 分支清理 | [stage3-bunkers.md](stage3-bunkers.md) Part D |

➡️ 回家 2 小時:[作業二](homework/homework2.md)

> 👩‍🏫 教學者請看 [teaching-plan.md](teaching-plan.md):設計理念、逐段帶課節奏與給新手的提醒。

## 環境準備(第一堂課前)

```bash
# 1. 安裝 Python(3.8 以上)與 Git
# 2. 安裝遊戲套件
python -m pip install pygame

# 3. 把這個 repo 抓下來
git clone <你的 repo 網址>
cd github-tutorial

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
