import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LogisticRegression, LinearRegression

from logic import model_eval
from logic.models import get_model_pipeline

data = load_diabetes()

features = data.feature_names
X = pd.DataFrame(data.data, columns=features)
y_reg = data.target
y_class = 1*(y_reg > 140)
features_num = ['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
features_cat = ['sex']


pipeline_class = get_model_pipeline(LogisticRegression, features_cat, features_num, {'random_state': 1234})
pipeline_reg = get_model_pipeline(LinearRegression, features_cat, features_num, {'random_state': 1234})
fitted_pipeline_class = pipeline_class.fit(X, y_class)
fitted_pipeline_reg = pipeline_reg.fit(X, y_reg)


def test_get_contingency_table():
    result = model_eval.get_contingency_table(X, y_class, 'classification', fitted_pipeline_class)
    expected_result = {'true_positive': 165, 'true_negative': 164, 'false_positive': 57, 'false_negative': 56}

    assert result == expected_result

    result = model_eval.get_contingency_table(X, y_reg, 'regression', fitted_pipeline_reg)
    expected_result = {'true_positive': None, 'true_negative': None, 'false_positive': None, 'false_negative': None}

    assert result == expected_result


def test_metric_evaluation():
    result = model_eval.metric_evaluation(y_class, pipeline_class.predict(X), 'roc_auc')
    expected_result = 74.434

    assert result == expected_result

    result = model_eval.metric_evaluation(y_reg, pipeline_reg.predict(X), 'mean_squared_error')
    expected_result = 285969.04

    assert result == expected_result


def test_get_metrics():
    result = model_eval.get_metrics(X, y_class, 'classification', fitted_pipeline_class)
    expected_result = {'roc_auc': 74.434, 'accuracy': 74.434, 'balanced_accuracy': 74.434, 'recall': 74.661,
                       'precision': 74.324, 'f1_score': 74.492}

    assert result == expected_result

    result = model_eval.get_metrics(X, y_reg, 'regression', fitted_pipeline_reg)
    expected_result = {'mean_squared_error': 285969.04, 'mean_absolute_error': 4327.74}

    assert result == expected_result


def test_get_roc_curve():
    result = model_eval.get_roc_curve(fitted_pipeline_class, X, y_class)
    expected_result = [{'fpr': 0.0, 'tpr': 0.0, 'threshold': 1.8080490673204934},
                       {'fpr': 0.0, 'tpr': 0.004524886877828055, 'threshold': 0.8080490673204934},
                       {'fpr': 0.0, 'tpr': 0.11312217194570136, 'threshold': 0.6887430888846666}]

    assert result[0:3] == expected_result

    try:
        model_eval.get_roc_curve(fitted_pipeline_class, X, y_reg)
    except ValueError as e:
        assert str(e) == 'multiclass format is not supported'


def test_get_pdps():
    result = model_eval.get_pdps(fitted_pipeline_class, X, features_cat, features_num)
    expected_result ={'feature': 'sex', 'pdp': [[-0.044641636506989, 0.0506801187398187], [0.48193877513423466, 0.5166505226129072]]}

    assert result[-1] == expected_result

    result = model_eval.get_pdps(fitted_pipeline_reg, X, features_cat, features_num)
    expected_result = {'feature': 'sex', 'pdp': [[-0.044641636506989, 0.0506801187398187], [146.05645420033423, 157.48644247034704]]}

    assert result[-1] == expected_result


def test_next_to_remove():
    result = model_eval.next_to_remove(X, y_class, X, y_class, features_cat, features_num, 'sex', LogisticRegression, 0.1, 'roc_auc')
    expected_result = {'feature_name': 'sex', 'metric_eval': 74.661, 'improvement': 74561.0, 'metric': 'roc_auc'}

    assert result == expected_result

    result = model_eval.next_to_remove(X, y_reg, X, y_reg, features_cat, features_num, 'sex', LinearRegression, 0.1, 'mean_squared_error')
    expected_result = {'feature_name': 'sex', 'metric_eval': 296150.023, 'improvement': 296149923.0, 'metric': 'mean_squared_error'}

    assert result == expected_result


def test_next_to_include():
    result = model_eval.next_to_include(X, y_class, X, y_class, features_cat, features_num, LogisticRegression, features_cat, features_num, 0.1, 'roc_auc')
    expected_result = None

    assert result == expected_result

    result = model_eval.next_to_include(X, y_class, X, y_class, features_cat, features_num[0:2], LogisticRegression, features_cat, features_num, 0.1, 'roc_auc')
    expected_result = {'feature_name': 's5', 'metric_eval': 74.208, 'improvement': 74108.0, 'metric': 'roc_auc'}

    assert result == expected_result


def test_fet_feature_importance():
    result = model_eval.get_feature_importance(fitted_pipeline_class, features, X, y_class)
    expected_result = [{'feature': 's5', 'importance': 0.0339366515837104}, {'feature': 's5', 'importance': 0.0339366515837104}, {'feature': 's5', 'importance': 0.02714932126696834}, {'feature': 's5', 'importance': 0.022624434389140302}, {'feature': 's5', 'importance': 0.011312217194570207}, {'feature': 's5', 'importance': 0.011312217194570207}, {'feature': 's5', 'importance': 0.020361990950226283}, {'feature': 's5', 'importance': 0.038461538461538436}, {'feature': 's5', 'importance': 0.013574660633484226}, {'feature': 's5', 'importance': 0.009049773755656076}, {'feature': 's5', 'importance': 0.02941176470588236}, {'feature': 's5', 'importance': 0.02941176470588236}, {'feature': 's5', 'importance': 0.013574660633484226}, {'feature': 's5', 'importance': 0.03619909502262442}, {'feature': 's5', 'importance': 0.04751131221719462}, {'feature': 'bmi', 'importance': 0.02488687782805432}, {'feature': 'bmi', 'importance': 0.022624434389140302}, {'feature': 'bmi', 'importance': 0.02488687782805432}, {'feature': 'bmi', 'importance': 0.0}, {'feature': 'bmi', 'importance': 0.011312217194570207}, {'feature': 'bmi', 'importance': 0.020361990950226283}, {'feature': 'bmi', 'importance': 0.03167420814479638}, {'feature': 'bmi', 'importance': 0.02488687782805432}, {'feature': 'bmi', 'importance': 0.038461538461538436}, {'feature': 'bmi', 'importance': 0.02488687782805432}, {'feature': 'bmi', 'importance': 0.02714932126696834}, {'feature': 'bmi', 'importance': 0.011312217194570207}, {'feature': 'bmi', 'importance': 0.022624434389140302}, {'feature': 'bmi', 'importance': 0.020361990950226283}, {'feature': 'bmi', 'importance': 0.03167420814479638}, {'feature': 'sex', 'importance': 0.004524886877828038}, {'feature': 'sex', 'importance': 0.011312217194570207}, {'feature': 'sex', 'importance': 0.02714932126696834}, {'feature': 'sex', 'importance': 0.015837104072398245}, {'feature': 'sex', 'importance': 0.02488687782805432}, {'feature': 'sex', 'importance': -0.002262443438914019}, {'feature': 'sex', 'importance': 0.02714932126696834}, {'feature': 'sex', 'importance': 0.02941176470588236}, {'feature': 'sex', 'importance': 0.0339366515837104}, {'feature': 'sex', 'importance': 0.018099547511312264}, {'feature': 'sex', 'importance': 0.022624434389140302}, {'feature': 'sex', 'importance': 0.02488687782805432}, {'feature': 'sex', 'importance': 0.0339366515837104}, {'feature': 'sex', 'importance': 0.015837104072398245}, {'feature': 'sex', 'importance': 0.015837104072398245}, {'feature': 'bp', 'importance': 0.022624434389140302}, {'feature': 'bp', 'importance': 0.020361990950226283}, {'feature': 'bp', 'importance': 0.013574660633484226}, {'feature': 'bp', 'importance': -0.009049773755656076}, {'feature': 'bp', 'importance': 0.009049773755656076}, {'feature': 'bp', 'importance': 0.040723981900452455}, {'feature': 'bp', 'importance': 0.011312217194570207}, {'feature': 'bp', 'importance': 0.020361990950226283}, {'feature': 'bp', 'importance': 0.0}, {'feature': 'bp', 'importance': 0.013574660633484226}, {'feature': 'bp', 'importance': 0.009049773755656076}, {'feature': 'bp', 'importance': 0.015837104072398245}, {'feature': 'bp', 'importance': 0.02714932126696834}, {'feature': 'bp', 'importance': 0.013574660633484226}, {'feature': 'bp', 'importance': 0.038461538461538436}, {'feature': 's3', 'importance': 0.018099547511312264}, {'feature': 's3', 'importance': 0.011312217194570207}, {'feature': 's3', 'importance': -0.004524886877828038}, {'feature': 's3', 'importance': 0.020361990950226283}, {'feature': 's3', 'importance': -0.009049773755656076}, {'feature': 's3', 'importance': 0.018099547511312264}, {'feature': 's3', 'importance': 0.002262443438914019}, {'feature': 's3', 'importance': 0.03167420814479638}, {'feature': 's3', 'importance': 0.0}, {'feature': 's3', 'importance': 0.002262443438914019}, {'feature': 's3', 'importance': -0.004524886877828038}, {'feature': 's3', 'importance': 0.0}, {'feature': 's3', 'importance': 0.015837104072398245}, {'feature': 's3', 'importance': -0.004524886877828038}, {'feature': 's3', 'importance': 0.006787330316742057}, {'feature': 'age', 'importance': 0.004524886877828038}, {'feature': 'age', 'importance': -0.004524886877828038}, {'feature': 'age', 'importance': -0.004524886877828038}, {'feature': 'age', 'importance': 0.0}, {'feature': 'age', 'importance': 0.004524886877828038}, {'feature': 'age', 'importance': -0.002262443438914019}, {'feature': 'age', 'importance': 0.009049773755656076}, {'feature': 'age', 'importance': 0.0}, {'feature': 'age', 'importance': 0.006787330316742057}, {'feature': 'age', 'importance': 0.002262443438914019}, {'feature': 'age', 'importance': 0.004524886877828038}, {'feature': 'age', 'importance': 0.009049773755656076}, {'feature': 'age', 'importance': 0.0}, {'feature': 'age', 'importance': 0.004524886877828038}, {'feature': 'age', 'importance': -0.002262443438914019}, {'feature': 's4', 'importance': 0.002262443438914019}, {'feature': 's4', 'importance': 0.009049773755656076}, {'feature': 's4', 'importance': -0.006787330316742057}, {'feature': 's4', 'importance': 0.011312217194570207}, {'feature': 's4', 'importance': 0.002262443438914019}, {'feature': 's4', 'importance': 0.009049773755656076}, {'feature': 's4', 'importance': -0.004524886877828038}, {'feature': 's4', 'importance': 0.002262443438914019}, {'feature': 's4', 'importance': -0.015837104072398134}, {'feature': 's4', 'importance': -0.009049773755656076}, {'feature': 's4', 'importance': 0.004524886877828038}, {'feature': 's4', 'importance': -0.004524886877828038}, {'feature': 's4', 'importance': 0.015837104072398245}, {'feature': 's4', 'importance': -0.013574660633484115}, {'feature': 's4', 'importance': 0.022624434389140302}, {'feature': 's6', 'importance': 0.002262443438914019}, {'feature': 's6', 'importance': -0.002262443438914019}, {'feature': 's6', 'importance': 0.006787330316742057}, {'feature': 's6', 'importance': -0.002262443438914019}, {'feature': 's6', 'importance': 0.0}, {'feature': 's6', 'importance': -0.006787330316742057}, {'feature': 's6', 'importance': -0.015837104072398134}, {'feature': 's6', 'importance': 0.002262443438914019}, {'feature': 's6', 'importance': 0.0}, {'feature': 's6', 'importance': 0.002262443438914019}, {'feature': 's6', 'importance': 0.0}, {'feature': 's6', 'importance': -0.004524886877828038}, {'feature': 's6', 'importance': -0.011312217194570096}, {'feature': 's6', 'importance': 0.006787330316742057}, {'feature': 's6', 'importance': 0.0}, {'feature': 's1', 'importance': -0.002262443438914019}, {'feature': 's1', 'importance': -0.002262443438914019}, {'feature': 's1', 'importance': 0.002262443438914019}, {'feature': 's1', 'importance': -0.006787330316742057}, {'feature': 's1', 'importance': 0.002262443438914019}, {'feature': 's1', 'importance': -0.004524886877828038}, {'feature': 's1', 'importance': 0.0}, {'feature': 's1', 'importance': -0.002262443438914019}, {'feature': 's1', 'importance': -0.002262443438914019}, {'feature': 's1', 'importance': -0.004524886877828038}, {'feature': 's1', 'importance': -0.011312217194570096}, {'feature': 's1', 'importance': 0.002262443438914019}, {'feature': 's1', 'importance': -0.006787330316742057}, {'feature': 's1', 'importance': -0.004524886877828038}, {'feature': 's1', 'importance': 0.004524886877828038}, {'feature': 's2', 'importance': -0.006787330316742057}, {'feature': 's2', 'importance': 0.002262443438914019}, {'feature': 's2', 'importance': 0.004524886877828038}, {'feature': 's2', 'importance': -0.009049773755656076}, {'feature': 's2', 'importance': -0.002262443438914019}, {'feature': 's2', 'importance': 0.0}, {'feature': 's2', 'importance': -0.004524886877828038}, {'feature': 's2', 'importance': -0.002262443438914019}, {'feature': 's2', 'importance': -0.002262443438914019}, {'feature': 's2', 'importance': 0.002262443438914019}, {'feature': 's2', 'importance': -0.006787330316742057}, {'feature': 's2', 'importance': -0.002262443438914019}, {'feature': 's2', 'importance': -0.011312217194570096}, {'feature': 's2', 'importance': -0.002262443438914019}, {'feature': 's2', 'importance': 0.002262443438914019}]

    assert result == expected_result

    result = model_eval.get_feature_importance(fitted_pipeline_reg, features, X, y_reg)
    expected_result = [{'feature': 's1', 'importance': 0.44937787700353504}, {'feature': 's1', 'importance': 0.5292557213444374}, {'feature': 's1', 'importance': 0.5336109880831078}, {'feature': 's1', 'importance': 0.46444011091517445}, {'feature': 's1', 'importance': 0.43506275179762477}, {'feature': 's1', 'importance': 0.5842532449161532}, {'feature': 's1', 'importance': 0.46542956015654413}, {'feature': 's1', 'importance': 0.47894076176671296}, {'feature': 's1', 'importance': 0.48157619503544524}, {'feature': 's1', 'importance': 0.502493022474615}, {'feature': 's1', 'importance': 0.5164685110358745}, {'feature': 's1', 'importance': 0.4722927056233117}, {'feature': 's1', 'importance': 0.4553241896075707}, {'feature': 's1', 'importance': 0.4720177972089965}, {'feature': 's1', 'importance': 0.537900281450259}, {'feature': 's5', 'importance': 0.43747606638388015}, {'feature': 's5', 'importance': 0.4163183570463057}, {'feature': 's5', 'importance': 0.4119853738349357}, {'feature': 's5', 'importance': 0.40308684639704884}, {'feature': 's5', 'importance': 0.397162323357812}, {'feature': 's5', 'importance': 0.41542905322465373}, {'feature': 's5', 'importance': 0.4044776370329237}, {'feature': 's5', 'importance': 0.4592522217564182}, {'feature': 's5', 'importance': 0.4121321330850384}, {'feature': 's5', 'importance': 0.3758959924758817}, {'feature': 's5', 'importance': 0.5129199543520572}, {'feature': 's5', 'importance': 0.4552942490961037}, {'feature': 's5', 'importance': 0.4379002727827974}, {'feature': 's5', 'importance': 0.4158964364190084}, {'feature': 's5', 'importance': 0.46461267040446186}, {'feature': 'bmi', 'importance': 0.2346940922160491}, {'feature': 'bmi', 'importance': 0.19545552038657155}, {'feature': 'bmi', 'importance': 0.2022202114061662}, {'feature': 'bmi', 'importance': 0.1873550233825353}, {'feature': 'bmi', 'importance': 0.18606988115968304}, {'feature': 'bmi', 'importance': 0.21974302807840707}, {'feature': 'bmi', 'importance': 0.21830607699129234}, {'feature': 'bmi', 'importance': 0.23003029745283932}, {'feature': 'bmi', 'importance': 0.2213415031934407}, {'feature': 'bmi', 'importance': 0.2122730784910667}, {'feature': 'bmi', 'importance': 0.2287725218619462}, {'feature': 'bmi', 'importance': 0.2028905300325834}, {'feature': 'bmi', 'importance': 0.22952004426071027}, {'feature': 'bmi', 'importance': 0.1925924913496282}, {'feature': 'bmi', 'importance': 0.2637589185676519}, {'feature': 's2', 'importance': 0.1784088708718965}, {'feature': 's2', 'importance': 0.17273822938112282}, {'feature': 's2', 'importance': 0.17835777553766596}, {'feature': 's2', 'importance': 0.15338502626101858}, {'feature': 's2', 'importance': 0.1938871969831607}, {'feature': 's2', 'importance': 0.1482585508987928}, {'feature': 's2', 'importance': 0.17956798076559877}, {'feature': 's2', 'importance': 0.15462987147412466}, {'feature': 's2', 'importance': 0.14833494742492281}, {'feature': 's2', 'importance': 0.20952923391267309}, {'feature': 's2', 'importance': 0.14643677825573276}, {'feature': 's2', 'importance': 0.17877404403592123}, {'feature': 's2', 'importance': 0.20919231184404785}, {'feature': 's2', 'importance': 0.16684349740825355}, {'feature': 's2', 'importance': 0.17035482158686077}, {'feature': 'bp', 'importance': 0.08972830929813913}, {'feature': 'bp', 'importance': 0.08967952685327624}, {'feature': 'bp', 'importance': 0.07187017131647794}, {'feature': 'bp', 'importance': 0.06770647686307446}, {'feature': 'bp', 'importance': 0.08714078778700252}, {'feature': 'bp', 'importance': 0.08509996343306991}, {'feature': 'bp', 'importance': 0.09419113056420897}, {'feature': 'bp', 'importance': 0.08494040907801576}, {'feature': 'bp', 'importance': 0.08307465155048754}, {'feature': 'bp', 'importance': 0.06809506081567113}, {'feature': 'bp', 'importance': 0.08805209446512524}, {'feature': 'bp', 'importance': 0.08766995412701889}, {'feature': 'bp', 'importance': 0.08441249910847665}, {'feature': 'bp', 'importance': 0.1029732820720699}, {'feature': 'bp', 'importance': 0.09054814472688327}, {'feature': 'sex', 'importance': 0.05292354438344027}, {'feature': 'sex', 'importance': 0.040868582071855175}, {'feature': 'sex', 'importance': 0.041939671136739465}, {'feature': 'sex', 'importance': 0.04488772276960157}, {'feature': 'sex', 'importance': 0.048267028366773934}, {'feature': 'sex', 'importance': 0.04056187213015833}, {'feature': 'sex', 'importance': 0.04622492018249136}, {'feature': 'sex', 'importance': 0.057222632783776095}, {'feature': 'sex', 'importance': 0.04457073478920426}, {'feature': 'sex', 'importance': 0.04272913406327278}, {'feature': 'sex', 'importance': 0.056538122490934595}, {'feature': 'sex', 'importance': 0.0384797326907475}, {'feature': 'sex', 'importance': 0.06974425721269645}, {'feature': 'sex', 'importance': 0.036874306140919966}, {'feature': 'sex', 'importance': 0.038619865357646666}, {'feature': 's4', 'importance': 0.024185278444738778}, {'feature': 's4', 'importance': 0.025985712039089837}, {'feature': 's4', 'importance': 0.01949619849076567}, {'feature': 's4', 'importance': 0.01875123574217269}, {'feature': 's4', 'importance': 0.024118999041112865}, {'feature': 's4', 'importance': 0.01808952463566932}, {'feature': 's4', 'importance': 0.02113552224975146}, {'feature': 's4', 'importance': 0.026840361208455732}, {'feature': 's4', 'importance': 0.018769534196476145}, {'feature': 's4', 'importance': 0.025619057298938097}, {'feature': 's4', 'importance': 0.022530353147744986}, {'feature': 's4', 'importance': 0.012583914041431776}, {'feature': 's4', 'importance': 0.02593167241459171}, {'feature': 's4', 'importance': 0.021998250027441435}, {'feature': 's4', 'importance': 0.0319283633816419}, {'feature': 's3', 'importance': 0.005137815050704542}, {'feature': 's3', 'importance': 0.005079138811522443}, {'feature': 's3', 'importance': 0.009263589187988086}, {'feature': 's3', 'importance': 0.012951473296257565}, {'feature': 's3', 'importance': 0.007450997510583535}, {'feature': 's3', 'importance': 0.006690600901691601}, {'feature': 's3', 'importance': 0.008563228164785608}, {'feature': 's3', 'importance': 0.00509887023072475}, {'feature': 's3', 'importance': 0.007759034708234469}, {'feature': 's3', 'importance': 0.006603677644051342}, {'feature': 's3', 'importance': 0.007114043745464094}, {'feature': 's3', 'importance': 0.01315778960404368}, {'feature': 's3', 'importance': 0.011571866006924947}, {'feature': 's3', 'importance': 0.010017521882669689}, {'feature': 's3', 'importance': 0.0010606597766921189}, {'feature': 's6', 'importance': 0.005216197566618508}, {'feature': 's6', 'importance': 0.006178748346092777}, {'feature': 's6', 'importance': 0.0034811453796291802}, {'feature': 's6', 'importance': 0.002458890808978098}, {'feature': 's6', 'importance': -0.0010441403280453398}, {'feature': 's6', 'importance': 0.0015331376717950818}, {'feature': 's6', 'importance': 0.0064262146910690765}, {'feature': 's6', 'importance': 0.00458727108063306}, {'feature': 's6', 'importance': 0.0035261577607673678}, {'feature': 's6', 'importance': -8.99318633512669e-05}, {'feature': 's6', 'importance': 0.005392089028896874}, {'feature': 's6', 'importance': 0.003344810792388242}, {'feature': 's6', 'importance': 0.006738763268400283}, {'feature': 's6', 'importance': 0.010383139454335333}, {'feature': 's6', 'importance': 0.007795802731332402}, {'feature': 'age', 'importance': 0.0001398971384786174}, {'feature': 'age', 'importance': 0.0004641548098555104}, {'feature': 'age', 'importance': -0.0004906143763684367}, {'feature': 'age', 'importance': 0.0005740700239319496}, {'feature': 'age', 'importance': -0.0002258231663708754}, {'feature': 'age', 'importance': -0.00046004821016720765}, {'feature': 'age', 'importance': -8.548694081744745e-05}, {'feature': 'age', 'importance': -0.0003061532519237353}, {'feature': 'age', 'importance': -0.00015336177012281738}, {'feature': 'age', 'importance': -0.0003423245195786073}, {'feature': 'age', 'importance': 0.00044019884565305034}, {'feature': 'age', 'importance': -0.0005326453735566838}, {'feature': 'age', 'importance': -0.00027191307945095833}, {'feature': 'age', 'importance': 0.0003033016228400909}, {'feature': 'age', 'importance': 0.0004148171272390089}]

    assert result == expected_result
