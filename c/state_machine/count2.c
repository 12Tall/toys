#include<stdio.h>
typedef unsigned char State;
typedef State (* Procedure)(void*);

// 注意这里有空格的，_ 代表参数，宏定义注释不要跟在后面
#define STATE_LIST(_) \
_(init)\
_(count)\
_(done)\
_(dft)

// 把0 强制转化为空字符
#define Step_NULL ((void *)0)

// 函数声明的宏定义
#define STATEMENT_STEP(state) \
State Step##_##state(void * arg);
STATE_LIST(STATEMENT_STEP)
#undef STATEMENT_STEP

#define DEFINE_STATE(state) State##_##state,

// # 将参数字符串化
// ## 将两个参数连为一个整体 
// ⚠: State 是字符串，state 是参数
enum States
{
	STATE_LIST(DEFINE_STATE)
	// 宏定义内引用宏定义，第一层展开后
	// DEFINE_STATE(init),
	// DEFINE_STATE(count),
	// DEFINE_STATE(done),
	// DEFINE_STATE(dft),

	// 第二层展开后
	// State_init,
	// State_count,
	// State_done,
	// State_deft,

	State_Nums
};

// 解除宏定义
#undef DEFINE_STATE

// 函数表
#define STATE_PROCEDURE(state) Step##_##state,
Procedure Steps[] = {
	STATE_LIST(STATE_PROCEDURE)
	// Step_NULL
	// 这里需要类型转换
	(Procedure)Step_NULL
};
#undef STATE_PROCEDURE

// 参数定义
typedef struct _SM_VAR
{
	int cnt;
} SM_VAR;

void BestStateMachine(void* invar)
{
	static State NS = State_init;
	NS = Steps[NS](invar);
}

int main(void)
{
	SM_VAR var;
	int i;
	for (i = 0; i <= 8; i++)
	{
		BestStateMachine(&var);
	}
	return 0;
}

State Step_init(void* arg) //初始化
{
	SM_VAR* p = (SM_VAR *)arg;
	p->cnt = 0;
	printf("CS:init ;cnt=%d;NS:count\n", p->cnt);
	return State_count;
}

State Step_count(void* arg) //计数
{
	SM_VAR* p = (SM_VAR *)arg;
	if (p->cnt < 3)
	{
		p->cnt += 1;
		printf("CS:count;cnt=%d;NS:count\n", p->cnt);
		return State_count;
	}
	else
	{
		printf("CS:count;cnt=%d;NS:done\n", p->cnt);
		return State_done;
	}
}

State Step_done(void* arg) //计数完成
{
	SM_VAR* p = (SM_VAR *)arg;
	printf("CS:done ;cnt=%d;NS:init\n", p->cnt);
	return State_init;
}

State Step_dft(void* arg) //错误过程
{
	SM_VAR* p = (SM_VAR *)arg;
	printf("Wrong State\n");
	return State_init;
}
