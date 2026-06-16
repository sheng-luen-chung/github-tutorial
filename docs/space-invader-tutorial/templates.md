# Issue / PR / Commit 範本(直接複製)

新手最常卡在「不知道要寫什麼」。下面都可以複製貼上後改一兩個字。

---

## Issue 範本

```
標題:加入關卡系統

## 想做什麼
清空一波敵人後不要結束遊戲,改成進入下一關。

## 細節
- 關卡數 +1 並顯示在畫面上方
- 每過一關敵人速度 +1
- 重新開始時關卡與速度歸 1

## 完成標準
打完一波後看到 Level 2,且敵人明顯變快。
```

---

## Pull Request 範本

```
標題:玩家三條命

## 這個 PR 做了什麼
讓玩家被擊中三次才結束,並在右上角顯示剩餘生命。

## 怎麼測試
1. python space_invader.py
2. 故意被敵人子彈打中
3. 確認 Lives 從 3 遞減,歸零才 GAME OVER

## 相關 Issue
Closes #1
```

> 把 `Closes #1` 寫進 PR 內文或 commit 訊息,merge 後對應 Issue 會自動關閉。

---

## Commit 訊息慣例

格式:`類型: 簡短描述`(動詞開頭,說清楚做了什麼)

| 類型 | 用在 | 範例 |
|------|------|------|
| `feat` | 新功能 | `feat: 玩家三條命並顯示在右上角` |
| `fix` | 修 bug | `fix: 子彈飛出畫面後沒有被移除` |
| `refactor` | 重整程式但功能不變 | `refactor: 把生成敵人抽成 spawn_enemies()` |
| `docs` | 改文件 | `docs: 補上階段二教學說明` |
| `style` | 只改外觀/排版 | `style: 分數改成黃色` |

**好 vs 不好:**

- ✅ `feat: 加入防護罩,可擋下敵人子彈`
- ❌ `update`、`改一下`、`123`、`aaa`

---

## 常用指令速查

```bash
git status                 # 現在改了哪些檔案
git branch                 # 我在哪條分支(* 那條)
git checkout -b 名稱        # 建立並切換到新分支
git add 檔名               # 把改動放進「準備存檔」區
git commit -m "訊息"       # 拍一張快照
git push -u origin 分支名   # 第一次上傳分支
git push                   # 之後上傳
git pull                   # 抓 GitHub 最新版
git log --oneline          # 一行一個看 commit 歷史
git checkout main          # 切回 main
```

---

## 卡住時的求救順序

1. `git status` —— 它通常會直接告訴你下一步該做什麼。
2. 看畫面紅字的最後一行,那是真正的錯誤訊息。
3. 對照 `solutions/` 裡的解答檔。
4. 還是不行 —— 截圖問老師/助教,附上 `git status` 的結果。
