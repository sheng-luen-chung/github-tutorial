# Space Invader 🚀

用 Python + pygame 寫的小型 Space Invader 遊戲,並搭配一套 **Git / GitHub 三小時教程** ——
適合剛上大一、想一邊做遊戲一邊把 GitHub 協作流程練熟的新手。

## 玩法

- `←` `→`:移動太空船
- `空白鍵`:發射子彈
- `R`:遊戲結束後重新開始

擊落所有敵人前別讓它們碰到你或衝到底部!

## 安裝與執行

```bash
python -m pip install pygame
python space_invader.py
```

## 三小時教程

跟著 [`docs/space-invader-tutorial/`](docs/space-invader-tutorial/README.md) 走,你會在三個階段裡反覆練習完整的 GitHub 協作循環:

```
開 Issue → 開 branch → 改程式 → commit → push → 開 PR → merge → 切回 main → pull
```

| 階段 | 遊戲功能 | Git 重點 |
|------|----------|----------|
| [階段一](docs/space-invader-tutorial/stage1-lives.md) | 玩家三條命 | 完整跑一次循環 + 第一個 PR |
| [階段二](docs/space-invader-tutorial/stage2-levels.md) | 關卡系統 | 用 Issue 追蹤 + 好的 commit |
| [階段三](docs/space-invader-tutorial/stage3-bunkers.md) | 防護罩 + 爆炸特效 | 解決 merge 衝突 + `.gitignore` |

## 專案結構

```
space_invader.py                    遊戲起點(教程從這份開始改)
solutions/                          各階段解答程式碼
docs/space-invader-tutorial/        教程講義與 Issue/PR 範本
```
