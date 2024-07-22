# SKN01-3nd-5Team
SKN01-3nd-5Team

# 1. Introduction Team (팀 소개)
- ### Chat-gtp(great-taking-potato)

| 김용현 | 김지민 | 한병찬 | 이용우 | 정원형|
|:----------:|:----------:|:----------:|:----------:|:----------:|
| <img width="120px" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/33ea2a85-1853-484b-b2a4-c750f854a26b" /> | <img width="120px" src="https://github.com/user-attachments/assets/628ab454-d1b8-41d3-88fc-a013ade00cb7" /> | <img width="120px" src="https://github.com/younghyen7956/study/assets/155882166/cd405d10-d646-4ba8-bda8-051f24d1bf30" /> |  <img width="120px" src="https://github.com/younghyen7956/study/assets/155882166/68939030-b840-4e41-8970-afe6cdbce4d5" /> | <img width="120px" src="https://github.com/user-attachments/assets/2c462581-5fae-46a3-b314-d09dfde4dd0d" /> |
| [@younghyen7956](https://github.com/younghyen7956) | [@jimin9703](https://github.com/jimin9703) | [@onebottlekick](https://github.com/onebottlekick) | [@lyw00](https://github.com/lyw00) | [@wh5905](https://github.com/wh5905) |
# 2. Introduction Project (프로젝트 개요)

# CI/CD 프로젝트 개요

**CI/CD**는 "Continuous Integration"과 "Continuous Deployment"의 약자로, 소프트웨어 개발 및 배포의 효율성을 높이기 위한 자동화된 프로세스를 의미합니다. CI/CD는 개발자가 코드를 지속적으로 통합하고, 이를 자동으로 테스트 및 배포하여 신속하고 안정적인 소프트웨어 제공을 목표로 합니다.

## 프로젝트 소개
이 **CI/CD 프로젝트**는 개발팀의 소프트웨어 개발 라이프사이클을 자동화하고 최적화하기 위해 설계되었습니다. CI/CD 파이프라인은 코드의 변경 사항을 실시간으로 감지하고, 이를 자동으로 빌드, 테스트, 배포하는 일련의 자동화된 프로세스를 포함합니다. 이 프로젝트는 다양한 도구와 플랫폼(예: Jenkins, GitLab CI, GitHub Actions, CircleCI 등)을 활용하여 효과적인 CI/CD 환경을 구축하고, 개발팀의 생산성을 극대화하는 것을 목표로 합니다.

## 필요성

1. **효율적인 코드 통합**: 개발자들이 코드 변경 사항을 자주 통합할 수 있도록 하여 코드의 충돌을 사전에 예방하고, 코드 품질을 유지합니다.
2. **빠른 피드백 루프**: 자동화된 테스트와 빌드 프로세스를 통해 코드 변경 후 신속하게 피드백을 제공함으로써 버그를 조기에 발견하고 수정할 수 있습니다.
3. **배포의 자동화**: 배포 과정을 자동화하여 배포의 일관성을 높이고, 수동 오류를 줄이며, 새로운 기능이나 버그 수정을 신속하게 사용자에게 제공할 수 있습니다.
4. **비즈니스 민첩성 향상**: CI/CD를 통해 개발 주기를 단축시키고, 시장의 요구에 빠르게 대응할 수 있습니다.

## 목표

1. **자동화된 테스트 및 빌드**: 코드가 변경될 때마다 자동으로 테스트를 수행하고, 성공적인 경우에만 빌드를 진행하여 안정성을 보장합니다.
2. **지속적인 배포**: 성공적인 빌드 후 자동으로 배포를 진행하여 소프트웨어를 신속하게 사용자에게 제공할 수 있도록 합니다.
3. **통합 환경 제공**: 다양한 개발 및 배포 도구를 통합하여 일관된 CI/CD 환경을 구축하고, 개발팀 간의 협업을 촉진합니다.
4. **문서화 및 모니터링**: CI/CD 파이프라인의 각 단계를 문서화하고, 모니터링 시스템을 구축하여 문제를 조기에 발견하고 해결할 수 있도록 합니다.
5. **변경 사항의 투명성 제공**: CI/CD 파이프라인을 통해 코드 변경 사항과 배포 상태를 명확하게 관리하고, 팀원들과 이해관계자들에게 투명한 정보를 제공합니다.

이 프로젝트는 CI/CD 프로세스를 통해 개발의 효율성과 품질을 높이고, 고객에게 더 나은 소프트웨어를 제공하기 위한 필수적인 기반을 마련하는 데 중점을 둡니다.


# 3. ERD 구성
<div style="text-align: center;">
  <img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-1st-5Team/assets/168423037/0c38f744-c977-4807-a6d2-92ff0b68b68c" alt="img">
</div>

## 애자일 보드를 사용하는 이유
```c
과거 정의서들을 일일히 작성하였지만 빠른 속도로 무언가를 개발하는데 한계가 있습니다.
처음부터 많은 것들을 빌드업하면서 빠른 생산성을 기반으로 움직이려면 반드시 애자일해야합니다.
고로 폭포수 설계 방식이 아닌 애자일 프로세스 방식으로 애자일 보드를 작성하면서 진행했습니다.

애자일 보드는 자체적으로 제목이 요구 사항을 내포하며 각 카드 내부에는 정의한 Domain의 세부 사항이 기록됩니다.
고로 빠르게 팀원들과 협업 할 수 있고 소통 비용을 최소화시킬 수 있습니다.
작은 것 같지만 이와 같은 것들이 쌓여서 아주 기민하고 민첩한 조직을 만들어 냅니다.
```

# 4. Backend 애자일 보드 - 요구 사항 정의서
![backend](https://github.com/user-attachments/assets/c5bc9c8f-b6de-4194-b8d9-0b97e5345ed7)

# 5. Frontend 애자일 보드 - 화면 설계서
![frontend1](https://github.com/user-attachments/assets/4294699e-0223-493f-8295-a673a4a79660)
![frontend2](https://github.com/user-attachments/assets/dc54b20e-e5a7-4772-aca5-e4fc5ebc40f3)
# 6. FastAPI 애자일 보드 - AI 서빙 설계서

# 7. 시스템 구성도
![image](https://github.com/user-attachments/assets/5385f5b5-fbd1-41b9-bbec-eea1a607c67b)

# 8. Manual Deploy (수동 배포 진행 절차)

## Frontend (UI)

## Backend (Server)

## FastAPI (AI Core Server)

# 9. Autonomous Deploy (자동 배포 진행 절차)

## Frontend (UI)

## Backend (Server)

## FastAPI (AI Core Server)

# 10. Result (수행 결과)
### 메인 화면
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-1st-5Team/assets/168423037/eadc16be-2c03-401d-b4b9-27ffbb6cd5c9"/>

### 개인별 호텔 추천 서비스
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/168423037/0215b44b-b0aa-48be-833d-4a7a5602fd52"/>

### AARRR 분석 페이지
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/168423037/ff46ab8d-00bb-4c4a-b875-17162b703ff6"/>
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/168423037/caa0dc76-b158-4293-b0b7-a70ab87bfb13"/>

# 11. Tech Stack (기술 스택)
### Backend
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"/> ![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) <img src="https://img.shields.io/badge/pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/numpy-%23013243?style=for-the-badge&logo=numpy&logoColor=white"/>

### Frontend
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=black"/> <img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"/> <img src="https://img.shields.io/badge/vuetify-%231867C0?style=for-the-badge&logo=vuetify&logoColor=white"/> <img src="https://img.shields.io/badge/axios-%235A29E4?style=for-the-badge&logo=axios&logoColor=white"/>

### Communication
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) <img src="https://img.shields.io/badge/notion-%23000000?style=for-the-badge&logo=notion&logoColor=white"/> <img src="https://img.shields.io/badge/slack-%234A154B?style=for-the-badge&logo=slack&logoColor=white"/> ![GitKraken](https://img.shields.io/badge/GitKraken-179287?style=for-the-badge&logo=gitkraken&logoColor=white) ![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

### IDE
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=vscode&logoColor=white) <img src="https://img.shields.io/badge/pycharm-%23000000?style=for-the-badge&logo=pycharm&logoColor=white"/>

### MachingLearing
<img src="https://img.shields.io/badge/fastapi-%23009688?style=for-the-badge&logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/scikitlearn-%23F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>

### Infrastructure
<img src="https://img.shields.io/badge/docker-%232496ED?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/redis-%23FF4438?style=for-the-badge&logo=redis&logoColor=white"/> ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Graphviz](https://img.shields.io/badge/Graphviz-used-blue.svg) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

# 12. 테스트 보고서 (CI 테스트 결과)
CI 테스트 결과

![image1](https://github.com/user-attachments/assets/3148084b-c313-4f5c-8a24-4c2ec0a0e8d7)
*********
![image2](https://github.com/user-attachments/assets/c955dd4c-fee1-429a-a161-ea3a10cf519d)
*********
![image3-1](https://github.com/user-attachments/assets/19d4676e-1e6d-49aa-bfde-9e76fb2ecbbb)
*********
![image3-2](https://github.com/user-attachments/assets/0fc14c05-4705-466b-ba03-5c4830ebc903)
*********
![image3-3](https://github.com/user-attachments/assets/4b2dfe05-2bfe-43c8-8777-9dded01c055c)
*********
![image4](https://github.com/user-attachments/assets/c88d74c5-aee2-4138-939c-352406ecf34c)

# 13. Deploy Issue (배포 이슈)

## 우선 순위를 5 단계로 나눠서 관리  

```c
실제 서비스를 운영한다는 마인드로 현실 상황에서 발생하는 크고 작은 이슈들이 존재할 것입니다.
이 서비스들에서 회사 입장에서 매출에 중요한 것과 중요하지 않은 것들이 있을 것입니다.
이와 같은 사항들을 실질적으로 고려하여 이슈 관리를 진행합니다.
```
  
### 급하지않음
* 서비스가 가능하면서 사용자들은 불편함을 느끼지 못하여 매출에 지장이 전혀 없는 경우  
    ![issue1](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/126551524/464a12d6-26d4-4e2c-921f-f9ed95290370)
### 보통
* 서비스가 불가능하여 기능을 하지 못하지만 수정하기 어렵지 않은 경우
    ![issue2](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/126551524/606ce865-0868-4693-9ec4-1f8b04ca2fd8)
### 급함
* 개발 막바지, 서비스 배포 직전에 문제가 생겨서 기능을 하지 못하는 경우
   ![issue3](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/126551524/a134df1b-49f3-4e20-810a-8e1db446ee91)
### 매우 급함
* 개발 초반부터 문제가 생겨 이후 연관된 모든 개발 진행에 차질이 생기는 경우
    ![issue4](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-2nd-5Team/assets/126551524/27b56023-cc2c-4905-84b7-8b0e34e2710a)

### 추가적인 이슈 해결 과정


# 14. 한 줄 회고
- #### 김용현 
> 짧은 기간이였지만 CI/CD가 정확히 무엇이고 어떻게 동작하는지 배웠고 실제 웹이나 어플이 어떻게 시스템을 배포하는지 배우게 되었다.또한 github action을 사용하는 방법을 배우면서 다음 프로젝트에서 잘 사용해야겠다.
- #### 김지민
>  짧은 기간동안 많은 기능들을 구현하려고 하다보니 쉽진 않았지만 그래도 힘든만큼 성장하는 것이라고 생각해서 성공적으로 마무리한 것 같습니다.
- #### 한병찬 
> aws 배포를 하며 점점 성장해가는 느낌이 들었다.
- #### 이용우
> 그동안 수업을 통해 배운 부분을 직접 구현을 하는 경험을 통해 보다 잘 이해할 수 있었습니다
- #### 정원형
> CI/CD 구축하면서 AWS와 Docker를 통해 애플리케이션을 자동으로 빌드, 테스트, 배포하는 과정을 이해할 수 있었다.



