# Changelog

## 0.5.0 (2025-06-02)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/prelude-so/python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** update via SDK Studio ([89eb324](https://github.com/prelude-so/python-sdk/commit/89eb3248d31252d70799490dfdf6f29645f56e1b))


### Chores

* **ci:** fix installation instructions ([afe0c52](https://github.com/prelude-so/python-sdk/commit/afe0c524b286def7133c08b84e4f0679bd045b49))
* **ci:** upload sdks to package manager ([5f4eaa3](https://github.com/prelude-so/python-sdk/commit/5f4eaa3b2581ea51ff992504996d141759496b96))
* **docs:** grammar improvements ([79cf9fe](https://github.com/prelude-so/python-sdk/commit/79cf9fe6f5084631be0a6de5b7f334c0d8e554e3))

## 0.4.0 (2025-05-13)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/prelude-so/python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** update via SDK Studio ([f5acdc5](https://github.com/prelude-so/python-sdk/commit/f5acdc5257392c967647a7c90fd98d6744cf646d))


### Bug Fixes

* **package:** support direct resource imports ([d4aff2a](https://github.com/prelude-so/python-sdk/commit/d4aff2a21b2da1884f80a919de0d106b6864d4e7))
* **pydantic v1:** more robust ModelField.annotation check ([adc627b](https://github.com/prelude-so/python-sdk/commit/adc627b38a17ba32d1aa9beff2a55b20aee00588))


### Chores

* broadly detect json family of content-type headers ([f47f2a8](https://github.com/prelude-so/python-sdk/commit/f47f2a8bc4c86f1607c4da6286648f8f68309746))
* **ci:** add timeout thresholds for CI jobs ([86a95ec](https://github.com/prelude-so/python-sdk/commit/86a95ec72dee0ad1c2daef78f6abe57e37ba172b))
* **ci:** only use depot for staging repos ([a93504a](https://github.com/prelude-so/python-sdk/commit/a93504a8378b223e8dc1bd2aee69861faf6d6aa4))
* **ci:** run on more branches and use depot runners ([8e40b2f](https://github.com/prelude-so/python-sdk/commit/8e40b2f2078cea5af1c74748abf0445e877d08a0))
* **client:** minor internal fixes ([191826b](https://github.com/prelude-so/python-sdk/commit/191826b8f197fc684013eccb67785692964dc4a2))
* **internal:** avoid errors for isinstance checks on proxies ([ef6a146](https://github.com/prelude-so/python-sdk/commit/ef6a146fb76282a8dad0d1a7aac45092c9fdc034))
* **internal:** base client updates ([658c667](https://github.com/prelude-so/python-sdk/commit/658c6672d8cef3a53b0fb15de1f34f12de554e09))
* **internal:** bump pyright version ([30e6817](https://github.com/prelude-so/python-sdk/commit/30e6817c4d2bbf13e3e8832e626b827d60e221b9))
* **internal:** fix list file params ([82ee669](https://github.com/prelude-so/python-sdk/commit/82ee669ad5fca2d5f6e2a3a35f05642ba763a488))
* **internal:** import reformatting ([5ef2486](https://github.com/prelude-so/python-sdk/commit/5ef24860752772fec8898d25cb2772ed9131209a))
* **internal:** refactor retries to not use recursion ([200a5da](https://github.com/prelude-so/python-sdk/commit/200a5da2c4b3f5ad06fdf94ecd9ee86c77f4965a))
* **internal:** update models test ([f77a730](https://github.com/prelude-so/python-sdk/commit/f77a7309750298a75f77c60cb672630ba9085f69))
* **internal:** update pyright settings ([4393e83](https://github.com/prelude-so/python-sdk/commit/4393e83b8c2a5e6bc63235ecb0551adb9504c9ca))

## 0.3.0 (2025-04-11)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/prelude-so/python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** update via SDK Studio ([e8db40d](https://github.com/prelude-so/python-sdk/commit/e8db40d0c6bb7ed120d01c7a5133e84611fa2dc5))
* **api:** update via SDK Studio ([2738f74](https://github.com/prelude-so/python-sdk/commit/2738f749089da145689c78aabdedf810d3329826))


### Bug Fixes

* **ci:** ensure pip is always available ([#81](https://github.com/prelude-so/python-sdk/issues/81)) ([3496a08](https://github.com/prelude-so/python-sdk/commit/3496a088c4a51ff9755df7d5537031d2b66224b8))
* **ci:** remove publishing patch ([#82](https://github.com/prelude-so/python-sdk/issues/82)) ([00fa879](https://github.com/prelude-so/python-sdk/commit/00fa8799dc14bc3d2dae941485f2e3a24bfb2bf3))
* **perf:** optimize some hot paths ([6203988](https://github.com/prelude-so/python-sdk/commit/6203988ff6273cfe5135ec7d427c620a1094f6a1))
* **perf:** skip traversing types for NotGiven values ([e5a8fd5](https://github.com/prelude-so/python-sdk/commit/e5a8fd59dd7168e68ff026e9d11d796e3d002241))
* **types:** handle more discriminated union shapes ([#80](https://github.com/prelude-so/python-sdk/issues/80)) ([716195b](https://github.com/prelude-so/python-sdk/commit/716195b1874b4ec76cd39465810e3500c756eae8))


### Chores

* fix typos ([#83](https://github.com/prelude-so/python-sdk/issues/83)) ([ab98ad3](https://github.com/prelude-so/python-sdk/commit/ab98ad32961298cf1a2f47e6b3cc66a9f69cddbc))
* **internal:** bump rye to 0.44.0 ([#78](https://github.com/prelude-so/python-sdk/issues/78)) ([436ceca](https://github.com/prelude-so/python-sdk/commit/436ceca01c22fd4015010d5bd3852ce319d0ed65))
* **internal:** codegen related update ([#79](https://github.com/prelude-so/python-sdk/issues/79)) ([e5e9c6d](https://github.com/prelude-so/python-sdk/commit/e5e9c6d643232cad96a285dd7dc662f98684fbdc))
* **internal:** expand CI branch coverage ([#87](https://github.com/prelude-so/python-sdk/issues/87)) ([3edb1aa](https://github.com/prelude-so/python-sdk/commit/3edb1aab16d2b38705d64969e9ac70fe00951ee6))
* **internal:** reduce CI branch coverage ([70118ea](https://github.com/prelude-so/python-sdk/commit/70118ea5611c2f4337b21ac7da52a740bc52d7ff))
* **internal:** remove extra empty newlines ([#76](https://github.com/prelude-so/python-sdk/issues/76)) ([3e52319](https://github.com/prelude-so/python-sdk/commit/3e5231901ad7bcc6e06a4c82aeaa619f759434f7))
* **internal:** remove trailing character ([#84](https://github.com/prelude-so/python-sdk/issues/84)) ([526b990](https://github.com/prelude-so/python-sdk/commit/526b990f47cf42a44064d85ed2d8f9acbe35a609))
* **internal:** slight transform perf improvement ([#85](https://github.com/prelude-so/python-sdk/issues/85)) ([b77e93b](https://github.com/prelude-so/python-sdk/commit/b77e93ba797273dd8a145183d9b9c712659163cd))
* **tests:** improve enum examples ([#86](https://github.com/prelude-so/python-sdk/issues/86)) ([140d696](https://github.com/prelude-so/python-sdk/commit/140d6966a00666b4ade42fef7de7ec701cf697d3))

## 0.2.0 (2025-03-11)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/prelude-so/python-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** update via SDK Studio ([#74](https://github.com/prelude-so/python-sdk/issues/74)) ([f9658f1](https://github.com/prelude-so/python-sdk/commit/f9658f1ebacf25f72ae9a8e9076958055c2de570))
* **client:** allow passing `NotGiven` for body ([#64](https://github.com/prelude-so/python-sdk/issues/64)) ([b32f989](https://github.com/prelude-so/python-sdk/commit/b32f98934973c8c2cfacd3ad9a6c0817405ec3c9))
* **client:** send `X-Stainless-Read-Timeout` header ([#59](https://github.com/prelude-so/python-sdk/issues/59)) ([6dcc82a](https://github.com/prelude-so/python-sdk/commit/6dcc82a592bdad9316eae8ab7b93095d2176caf3))


### Bug Fixes

* **client:** mark some request bodies as optional ([b32f989](https://github.com/prelude-so/python-sdk/commit/b32f98934973c8c2cfacd3ad9a6c0817405ec3c9))


### Chores

* **docs:** update client docstring ([#70](https://github.com/prelude-so/python-sdk/issues/70)) ([61cec66](https://github.com/prelude-so/python-sdk/commit/61cec666606b1999db0d6c7bc08e77aa2aed869e))
* **internal:** bummp ruff dependency ([#58](https://github.com/prelude-so/python-sdk/issues/58)) ([2381d4a](https://github.com/prelude-so/python-sdk/commit/2381d4a22cfd032f97470e0d012b6fc8a133305c))
* **internal:** change default timeout to an int ([#56](https://github.com/prelude-so/python-sdk/issues/56)) ([160f11e](https://github.com/prelude-so/python-sdk/commit/160f11e767ab3d5f7f1fdd8e423a6277a651fc82))
* **internal:** codegen related update ([#63](https://github.com/prelude-so/python-sdk/issues/63)) ([0516484](https://github.com/prelude-so/python-sdk/commit/05164849027af87dba0911340086b7904a7171f2))
* **internal:** codegen related update ([#67](https://github.com/prelude-so/python-sdk/issues/67)) ([32798a9](https://github.com/prelude-so/python-sdk/commit/32798a95e57769f4fc29abac8ba2dcd58d55a6ef))
* **internal:** codegen related update ([#68](https://github.com/prelude-so/python-sdk/issues/68)) ([f921517](https://github.com/prelude-so/python-sdk/commit/f921517c1c0b0c8197886f6948cecf56a1fdea87))
* **internal:** codegen related update ([#71](https://github.com/prelude-so/python-sdk/issues/71)) ([ec7fd9f](https://github.com/prelude-so/python-sdk/commit/ec7fd9feb6f45caf98d9667072910b6a0ebfc25d))
* **internal:** fix devcontainers setup ([#65](https://github.com/prelude-so/python-sdk/issues/65)) ([da3f6c6](https://github.com/prelude-so/python-sdk/commit/da3f6c6f48241dfe0909aabeb3eec2ba83c0e8ef))
* **internal:** fix type traversing dictionary params ([#60](https://github.com/prelude-so/python-sdk/issues/60)) ([9bf6b95](https://github.com/prelude-so/python-sdk/commit/9bf6b958c8b1ac01d191fb3ffdad7beb9ad0f06a))
* **internal:** minor type handling changes ([#61](https://github.com/prelude-so/python-sdk/issues/61)) ([0639a28](https://github.com/prelude-so/python-sdk/commit/0639a28c925209b6d2adb2d3022f350044bf5995))
* **internal:** properly set __pydantic_private__ ([#66](https://github.com/prelude-so/python-sdk/issues/66)) ([affe056](https://github.com/prelude-so/python-sdk/commit/affe056afdc01fc46d7dc23a003b69bb8528c16d))
* **internal:** update client tests ([#62](https://github.com/prelude-so/python-sdk/issues/62)) ([6096c2a](https://github.com/prelude-so/python-sdk/commit/6096c2aff213dca771b4e8f8675569e1bc1d1edf))


### Documentation

* revise readme docs about nested params ([#72](https://github.com/prelude-so/python-sdk/issues/72)) ([bff24a7](https://github.com/prelude-so/python-sdk/commit/bff24a785fbd56e126249cbfbc8f2af5c179b8a6))
* update URLs from stainlessapi.com to stainless.com ([#69](https://github.com/prelude-so/python-sdk/issues/69)) ([f3c2dc7](https://github.com/prelude-so/python-sdk/commit/f3c2dc7a219c04490aa22cdab677410136dc09d3))

## 0.1.0 (2025-02-05)

Full Changelog: [v0.1.0-beta.1...v0.1.0](https://github.com/prelude-so/python-sdk/compare/v0.1.0-beta.1...v0.1.0)

### Features

* **api:** update via SDK Studio ([#54](https://github.com/prelude-so/python-sdk/issues/54)) ([882a265](https://github.com/prelude-so/python-sdk/commit/882a265dbfd660fa86be9fceafd3bf095f332a7f))


### Bug Fixes

* **tests:** make test_get_platform less flaky ([#50](https://github.com/prelude-so/python-sdk/issues/50)) ([97fe150](https://github.com/prelude-so/python-sdk/commit/97fe150523ae369a3c1729c8a64ddcdbc2660fc6))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#51](https://github.com/prelude-so/python-sdk/issues/51)) ([0730cb0](https://github.com/prelude-so/python-sdk/commit/0730cb06e3db10b3a2ab537a23eafbe469e6b316))
* **internal:** bump pyright dependency ([#47](https://github.com/prelude-so/python-sdk/issues/47)) ([4fade6c](https://github.com/prelude-so/python-sdk/commit/4fade6ce965301b6fd4285c6192ce81b078296d6))
* **internal:** minor formatting changes ([#53](https://github.com/prelude-so/python-sdk/issues/53)) ([a2296ef](https://github.com/prelude-so/python-sdk/commit/a2296ef6d9581d4557832e42d683ec6a503b9b2e))
* **internal:** minor style changes ([#52](https://github.com/prelude-so/python-sdk/issues/52)) ([04f378c](https://github.com/prelude-so/python-sdk/commit/04f378c43cdcc795ca4a4967075db0f1480bf358))


### Documentation

* **raw responses:** fix duplicate `the` ([#49](https://github.com/prelude-so/python-sdk/issues/49)) ([b76a3a0](https://github.com/prelude-so/python-sdk/commit/b76a3a0e0376777859a1e938015309fc569734b0))

## 0.1.0-beta.1 (2025-01-14)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-beta.1](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.7...v0.1.0-beta.1)

### Features

* **api:** update via SDK Studio ([#45](https://github.com/prelude-so/python-sdk/issues/45)) ([214aa99](https://github.com/prelude-so/python-sdk/commit/214aa996f4ffea2c40030b938f205562d608c144))


### Bug Fixes

* correctly handle deserialising `cls` fields ([#42](https://github.com/prelude-so/python-sdk/issues/42)) ([6511235](https://github.com/prelude-so/python-sdk/commit/65112351b9c6767bbd3447b17ebab220bf04e34d))


### Chores

* **internal:** update deps ([#44](https://github.com/prelude-so/python-sdk/issues/44)) ([3c88900](https://github.com/prelude-so/python-sdk/commit/3c8890016b22448529967e11b9082721f8c5954c))

## 0.1.0-alpha.7 (2025-01-08)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([#40](https://github.com/prelude-so/python-sdk/issues/40)) ([a16ad08](https://github.com/prelude-so/python-sdk/commit/a16ad08cc54132be9f0d3553b21d98ca983edcba))


### Bug Fixes

* **client:** only call .close() when needed ([#37](https://github.com/prelude-so/python-sdk/issues/37)) ([9d64934](https://github.com/prelude-so/python-sdk/commit/9d64934403b4cfa4becd15b3d4f9934354ce1135))


### Chores

* add missing isclass check ([#35](https://github.com/prelude-so/python-sdk/issues/35)) ([09b83f5](https://github.com/prelude-so/python-sdk/commit/09b83f50fd71367bee93758a31cd53621ba56ab3))
* **internal:** add support for TypeAliasType ([#31](https://github.com/prelude-so/python-sdk/issues/31)) ([a734093](https://github.com/prelude-so/python-sdk/commit/a7340937bba33d659b17e001c3dc98d7f4b8d009))
* **internal:** bump httpx dependency ([#36](https://github.com/prelude-so/python-sdk/issues/36)) ([39a4778](https://github.com/prelude-so/python-sdk/commit/39a4778690edc67b96e4b7a67e8d75b3d184502a))
* **internal:** bump pyright ([#29](https://github.com/prelude-so/python-sdk/issues/29)) ([d10ba94](https://github.com/prelude-so/python-sdk/commit/d10ba94c17a48a69d6de2551f91d417dfd1a14e2))
* **internal:** codegen related update ([#32](https://github.com/prelude-so/python-sdk/issues/32)) ([f68da06](https://github.com/prelude-so/python-sdk/commit/f68da06af9e1db5524256ee91adeb46746e2d9ce))
* **internal:** codegen related update ([#34](https://github.com/prelude-so/python-sdk/issues/34)) ([9ac58c5](https://github.com/prelude-so/python-sdk/commit/9ac58c502a1247208c6bc77d482f87b6389dd1a9))
* **internal:** codegen related update ([#39](https://github.com/prelude-so/python-sdk/issues/39)) ([655d237](https://github.com/prelude-so/python-sdk/commit/655d237f79cf048671378fdfa340b9c32cc36484))
* **internal:** fix some typos ([#33](https://github.com/prelude-so/python-sdk/issues/33)) ([f720959](https://github.com/prelude-so/python-sdk/commit/f72095954c5f648759c52261916944c4363f2614))


### Documentation

* fix typos ([#38](https://github.com/prelude-so/python-sdk/issues/38)) ([84b1be6](https://github.com/prelude-so/python-sdk/commit/84b1be6c4450fbed3d9436dc48ad22a10ec75e0d))

## 0.1.0-alpha.6 (2024-12-11)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([#27](https://github.com/prelude-so/python-sdk/issues/27)) ([e34eb1c](https://github.com/prelude-so/python-sdk/commit/e34eb1c2f450d5068cce21d414d3a4a04c3b0766))


### Chores

* **internal:** bump pydantic dependency ([#25](https://github.com/prelude-so/python-sdk/issues/25)) ([62168ae](https://github.com/prelude-so/python-sdk/commit/62168aeb00400db101ef33e54b8c3d8446bea8f4))
* make the `Omit` type public ([#23](https://github.com/prelude-so/python-sdk/issues/23)) ([b8aa425](https://github.com/prelude-so/python-sdk/commit/b8aa425a77c73290a46dba106cb7277e67d1bf0f))


### Documentation

* **readme:** fix http client proxies example ([#26](https://github.com/prelude-so/python-sdk/issues/26)) ([66ce358](https://github.com/prelude-so/python-sdk/commit/66ce358d153fef76d64827abe99907badb64d220))

## 0.1.0-alpha.5 (2024-12-03)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#20](https://github.com/prelude-so/python-sdk/issues/20)) ([2920a25](https://github.com/prelude-so/python-sdk/commit/2920a25772e640ee100d332658b79836ae0e6375))


### Chores

* **internal:** bump pyright ([#21](https://github.com/prelude-so/python-sdk/issues/21)) ([3af0b97](https://github.com/prelude-so/python-sdk/commit/3af0b979ddee008fc9dabd2a3d7ce78727df3e03))
* **internal:** exclude mypy from running on tests ([#18](https://github.com/prelude-so/python-sdk/issues/18)) ([375162d](https://github.com/prelude-so/python-sdk/commit/375162d3e52d77faeaf3970a531a32ef60a50815))

## 0.1.0-alpha.4 (2024-11-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#12](https://github.com/prelude-so/python-sdk/issues/12)) ([380ea22](https://github.com/prelude-so/python-sdk/commit/380ea22a509deeb05b9b27af7b21aae5a70b4380))
* **api:** update via SDK Studio ([#16](https://github.com/prelude-so/python-sdk/issues/16)) ([a885d0a](https://github.com/prelude-so/python-sdk/commit/a885d0a4aaa978adf582c8743011765dfc65614f))


### Chores

* **internal:** fix compat model_dump method when warnings are passed ([#13](https://github.com/prelude-so/python-sdk/issues/13)) ([7f9b088](https://github.com/prelude-so/python-sdk/commit/7f9b08842698d0eb6911464089583d56db63e0cf))
* rebuild project due to codegen change ([#10](https://github.com/prelude-so/python-sdk/issues/10)) ([afd8c51](https://github.com/prelude-so/python-sdk/commit/afd8c5127bce604ba78290aaf62659a3c02471a5))
* remove now unused `cached-property` dep ([#15](https://github.com/prelude-so/python-sdk/issues/15)) ([292303e](https://github.com/prelude-so/python-sdk/commit/292303e362071f1ba1d7ce2e8311653e4c4ec3f6))


### Documentation

* add info log level to readme ([#14](https://github.com/prelude-so/python-sdk/issues/14)) ([ee4b1b2](https://github.com/prelude-so/python-sdk/commit/ee4b1b2cbfbec80d0ec43cb8e7c54cd0acaad7b9))

## 0.1.0-alpha.3 (2024-11-14)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Chores

* update SDK settings ([#7](https://github.com/prelude-so/python-sdk/issues/7)) ([ea056d4](https://github.com/prelude-so/python-sdk/commit/ea056d4e561e83d012c758ffcc5b8b60c0be28f5))

## 0.1.0-alpha.2 (2024-11-14)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/prelude-so/python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/prelude-so/python-sdk/issues/4)) ([5dd93b2](https://github.com/prelude-so/python-sdk/commit/5dd93b2620abcec8e912c4c7019edaf6265b62a2))

## 0.1.0-alpha.1 (2024-11-13)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/prelude-so/python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([a12fb38](https://github.com/prelude-so/python-sdk/commit/a12fb38d4c48b0719866317a5255082e24e10924))
* **api:** update via SDK Studio ([6c7b477](https://github.com/prelude-so/python-sdk/commit/6c7b477531e451af0b8d2026439d90cf86927ba5))
* **api:** update via SDK Studio ([c4e8e64](https://github.com/prelude-so/python-sdk/commit/c4e8e6495a0144ee4cc15acef97dd19ec620a983))
* **api:** update via SDK Studio ([414794b](https://github.com/prelude-so/python-sdk/commit/414794bb59f6f7369e284c6d2397876af966654e))
* **api:** update via SDK Studio ([ceb12f0](https://github.com/prelude-so/python-sdk/commit/ceb12f0e846918722f0dd0a95f3621a933f865f1))
* **api:** update via SDK Studio ([7215a73](https://github.com/prelude-so/python-sdk/commit/7215a73eb5de3eb54c8b1fc061aa364858489dcf))
* **api:** update via SDK Studio ([c037337](https://github.com/prelude-so/python-sdk/commit/c0373374764304163e5b7de137408c88d35e7dc8))
* **api:** update via SDK Studio ([6e40de2](https://github.com/prelude-so/python-sdk/commit/6e40de26cdbc73a6e3bdff03e346dc34510d2eb3))
* **api:** update via SDK Studio ([e9fad9f](https://github.com/prelude-so/python-sdk/commit/e9fad9f7cd6638ef39b288d8f7d111a78d29fa43))
* **api:** update via SDK Studio ([85a6e9d](https://github.com/prelude-so/python-sdk/commit/85a6e9d7a923856748323abbe9c626dcff6f99bc))


### Chores

* configure new SDK language ([57c88b9](https://github.com/prelude-so/python-sdk/commit/57c88b95e0cbd5d6ea76e24019145ab5ed173438))
* go live ([#2](https://github.com/prelude-so/python-sdk/issues/2)) ([3109229](https://github.com/prelude-so/python-sdk/commit/3109229a622a9968d7d97709ccfedf84f4676335))
* rebuild project due to codegen change ([17c7b8a](https://github.com/prelude-so/python-sdk/commit/17c7b8a6dbc66b3c1db8560dee6633529e22bb0a))
