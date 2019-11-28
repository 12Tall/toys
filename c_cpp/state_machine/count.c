#include <stdio.h>
typedef unsigned char State;
typedef State(* Procedure)(void *);
enum states{s_init,s_count,s_done,s_default};  // 状态定义

typedef struct _SM_VAR {  // 状态机参数的封装
    int cnt;  // 计数
} SM_VAR;

State step_init(void * arg){
    // 参数类型转换
    SM_VAR * p = (SM_VAR *)arg;
    p->cnt = 0;
    printf("CS:init;cnt=%d;NS:count\n",p->cnt);
    return s_count;
};

// 计数
State step_count(void * arg){
    // 参数类型转换
    SM_VAR * p = (SM_VAR *)arg;

    // 这里是可以将next state 抽象出来的吧
    if(p->cnt < 3){
        p->cnt ++;
        // 输出当前状态，计数值
        printf("CS:count;cnt=%d;NS:count\n",p->cnt);
        return s_count;
    }else{
        printf("CS:count;cnt=%d;NS:done\n",p->cnt);
        return s_done;
    }
};

// 可以通过宏命令简化参数解析
// 结束
State step_done(void * arg){
    // 参数类型转换
    SM_VAR * p = (SM_VAR *)arg;
    printf("CS:done;cnt=%d;NS:init\n",p->cnt);
    return s_init;
}

// 异常处理
State step_default(void * arg){
    // 参数类型转换
    SM_VAR * p = (SM_VAR *)arg;
    printf("CS:error;cnt=%d;NS:init\n",p->cnt);
    return s_init;
}

// 定义处理函数数组，也就是状态机的本质
Procedure Steps[] = {step_init,step_count,step_done,step_default};

void BestStateMachine(void * invar){
    // ⚠：重点：这里用static 保证下一次调用时NS 依然存在，并保持上一次的值
    // 在debug 模式下可以观察到，此句并不执行
    static State NS = s_init;  // 定义下一状态
    // 状态机开始
    NS = Steps[NS](invar);
}

int main(void){
    SM_VAR var;
    int i;
    for (i = 0; i < 8; i++)
    {
        BestStateMachine(&var);
    }
    return 0;
}