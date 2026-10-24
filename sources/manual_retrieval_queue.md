# 需要用户手动查找的资料

截至 2026-09-26：仍缺全文 7 条（P0 5、P1 2），本轮新增请求 0、解决 0。既有用户提供的 14 条保留在 CSV；馆藏 Full view 与取得 PDF 分开计数。

| 优先级 | 资料 | DOI/编号 | 官方入口与新线索 | 当前阻断 |
| --- | --- | --- | --- | --- |
| P0 | Wind Effects on Car Stability; W. E. Lay; P. W. Lett; 1953 | 10.4271/530255 | [官方](https://doi.org/10.4271/530255); 暂无可验证全文入口 | Crossref exact DOI reconfirmed. Publisher PDF timed out; OpenAlex closed; Semantic Scholar returned no OA URL. SAE landing still has Published 1953 versus generated Citation 1906 conflict. No original acquired. |
| P0 | Development of Aerodynamic Disturbance Test Procedures. Volume I: Executive Summary; R. H. Klein; J. R. Hogue; 1979 | dot-hs-805-078 | [官方](https://trid.trb.org/View/143777); https://catalog.hathitrust.org/Record/005475553 | HathiTrust https://catalog.hathitrust.org/Record/005475553 identifies 1979 Volume I, 33 p., Michigan Full view https://babel.hathitrust.org/cgi/pt?id=mdp.39015075464894 ; reader returned HTTP 403. Google Play book Dfg5AQAAMAAJ is listed free (38 scanned pages); Books API returned 429. No PDF acquired; catalog Full view does not prove direct PDF download or redistribution permission. |
| P0 | Development of Aerodynamic Disturbance Test Procedures. Volume II: Technical Report; R. H. Klein; J. R. Hogue; 1979 | dot-hs-805-079 | [官方](https://trid.trb.org/View/144116); https://catalog.hathitrust.org/Record/005475554 | HathiTrust https://catalog.hathitrust.org/Record/005475554 identifies 1979 Volume II, 192 p., Michigan Full view https://babel.hathitrust.org/cgi/pt?id=mdp.39015075464886 ; reader returned HTTP 403. Google Play book avg5AQAAMAAJ is listed free (196 scanned pages); Books API returned 429. TRID/NASA pagination 188 differs from catalog/scanned pagination; original unavailable, difference unresolved. No PDF acquired. |
| P0 | Road vehicles — Sensitivity to lateral wind — Open-loop test method using wind generator input; ISO; 2010 | iso-12021-2010 | [官方](https://www.iso.org/standard/53602.html); 暂无可验证全文入口 | ISO official catalog https://www.iso.org/standard/53602.html checked: published 2010-12, confirmed 2023, 14 pages; preview/paid standard only. No DOI on official catalog and no lawful full standard acquired; national-adoption DOI must not replace ISO identity. |
| P0 | Experimental and Numerical Validation of a Wind Gust Facility; Raffaele Volpe; Arthur da Silva; Valérie Ferrand; Luis Le Moyne; 2013 | 10.1115/1.4023194 | [官方](https://doi.org/10.1115/1.4023194); http://oatao.univ-toulouse.fr/8416/1/Ferrand_8416.pdf; https://hal.science/hal-01920549/document | Crossref exact DOI reconfirmed. ASME PDF HTTP 403; OpenAlex and Semantic Scholar both identify http://oatao.univ-toulouse.fr/8416/1/Ferrand_8416.pdf (other-oa). HTTPS handshake and original HTTP URL timed out. HAL prior bot challenge retained; no bypass. No PDF acquired; other-oa is not a redistribution grant. |
| P1 | Vehicle Performance in Crosswinds; P. J. Milner; 1968 | trid-116341 | [官方](https://trid.trb.org/View/116341); 暂无可验证全文入口 | TRID https://trid.trb.org/View/116341 reconfirms Milner, Automobile Engineer 58, pp352-355, August 1968. Exact title/author PDF discovery yielded no verified primary full text. Retain scoped no_doi_confirmed from prior Crossref/DataCite checks; not proof that no DOI or OA can ever exist. |
| P1 | Aerodynamic Characterization of a Full-Scale Compact Car Exposed to Transient Crosswind; James R. Bell; Henning Wilhelmi; Daniela Heine; et al.; 2021 | 10.4271/06-14-01-0001 | [官方](https://doi.org/10.4271/06-14-01-0001); 暂无可验证全文入口 | Crossref exact DOI reconfirmed. Publisher PDF timed out; OpenAlex and Semantic Scholar provide no OA PDF. DLR author repository https://elib.dlr.de/142566/ explicitly has no full text. No original acquired. |

## 2026-10-13 定向复核

仍缺7份全文，新增/解决请求0。仅复核sae-530255和jfe-2013-volpe：前者聚合元数据无OA，后者OATAO链接单次超时；上表其他入口保留历史结果，并非今日重试。2条DOI重新核验，未取得PDF；禁止从目录/other-oa标记推定已下载或可再分发。见access_check_2026-10-13.json。

## 2026-10-14 定向目录核查

未取得新原文，仍缺7份。ISO目录预览/购买；DOT I/II公开目录不等于全文。技术卷新增检索标识PB80-118383 / N80-21219（NASA官方目录索引条目，printed298；非原报告），供合法馆藏检索。原有HathiTrust403/Google API429入口未重试。其他来源保留之前核查日期。

## 2026-10-15

Bell2021/Milner1968定向检查仍未取得全文，人工请求新增0/解决0，仍缺7份。S2遇429即停，未重试受限入口。8项已有原始数据请求另有learning/audits/reproduction_inputs.csv交付表；该表是策展人建议格式，不是收到的数据。

## 当前2026-10-21：Volpe2013已解决

历史上表中的Volpe2013缺档已解决：HAL公开API列出的直接文件普通GET成功，30页作者稿已验明并通读，CSV为resolved_oa_download。其PDF仅本机，未取得再分发许可。当前缺全文 **6条：P0 4/P1 2**；历史CSV仍21条，本轮新增0/解决1。其余6项未解决，不重试先前受保护入口。Lay DOI当日复核；DOT定向目录检索未取得原始报告，NASA书目不冒充原报告。

## 2026-10-25：两项核心待办的新入口

Lay1953：NII CiNii AA00831028（https://ci.nii.ac.jp/ncid/AA00831028）列SAE Transactions从Vol61(1953)起及相应实体馆藏；AIST公开装订刊清单（https://www.aist.go.jp/pdf/aist_j/lib/seihonlist.pdf）索引条目也列61起。仅作为合法馆藏查找线索，不证明已取得该文、可在线下载或有再分发许可；没有发出馆际/作者请求。

ISO2010：ANSI的BS ISO预览（https://webstore.ansi.org/preview-pages/BSI/preview_30202455.pdf）在web工具中可见9页，含ISO版本封面和前置内容/印刷第1页；不含完整后续程序/分析条款。本机一次普通下载403后停止，未存文件或hash、未重试。零售商“free”搜索片段不作OA证据，live页是单用户许可/地域不可购买；不替换ISO身份/版本。

当前仍缺6份完整原文（本轮新增/解决0），两项P3核心待办、9原始复现请求均保留。见access_check_2026-10-25.json。
