# 最小 Temporal RAG 候选过滤探针

本目录提供 M2 的零调用、零检索工程探针：它只对调用方已经提供的候选元数据作确定性准入判断，**不会**下载语料、查询外部服务或调用模型。因此通过测试只能说明时间过滤契约可运行，不能说明 Temporal RAG 的模型效果。

## 契约

`filter.admit_candidate(candidate, cutoff_date)` 要求候选提供四个可空的日级 ISO-8601 字段：`document_date`、`event_date`、`knowledge_valid_from` 与 `knowledge_valid_to`。安全默认 `unknown_date_policy="exclude"`：任一未知日期均排除，避免把无法审计的未来材料静默放入候选集。

- `document_date`、`event_date`、`knowledge_valid_from` 晚于截止日时排除；等于截止日允许。
- `knowledge_valid_to` 早于截止日时排除；等于截止日允许。
- 返回值含 `allowed` 和机器可读的 `reason`，供未来运行清单记录；本模块不对历史知识存在、行动者可达性或来源许可作出结论。

调用者仍须单独记录来源、版本、许可、事件/知识日期的证据依据，并在运行前满足相应的 Benchmark gate。
