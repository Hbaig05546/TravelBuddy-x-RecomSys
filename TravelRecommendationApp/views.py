''' /TravelRecommendationApp/models.py '''
import pandas as pd
import ast
from IPython.display import display
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetail
from TravelRecommendationApp.models import DreamDestination, RecommendedDestination_cat , RecommendedDestination_tag
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
dest_data = pd.DataFrame(list(PackageDetail.objects.all().values_list(
    'id', 'pTitle', 'pLocation', 'pdetails', 'pic', 'pCategory', 'amount')))


# def destination_category_add(request):
#     # selected_categories = [] no need of list
#     # if request.method == 'POST':
#     #     pass
#     # print(type(request.POST.getlist('category')))  ## list type
#     if request.method == 'POST':
#         drm_dest = DreamDestination(
#             tms_owner=request.user,
#             pTitle="sample_destination",
#             pLocation="sample_destination",
#             pdetails="sample_destination",
#             pic="sample_destination",
#             pCategory=sorted(request.POST.getlist('category')[:-1]),
#             amount=100000,
#         )
#         try:
#             # print(request.POST.getlist('category'))
#             drm_dest.save()
#         except:
#             DreamDestination.objects.filter(tms_owner=request.user).delete()
#             drm_dest.save()
#         return HttpResponseRedirect('/TravelRecommendationApp/recommend_category/')
#     else:
#         return render(request, 'destination_options.html')


def DestinationRecommend_category(request):
    context = {}
    # this will have tuple inside a list..hence double indexing..
    if request.method == 'POST':
        drm_dest = DreamDestination(
            tms_owner=request.user,
            pTitle="sample_destination",
            pLocation="sample_destination",
            pdetails="sample_destination",
            pic="sample_destination",
            pCategory=sorted(request.POST.getlist('category')[:-1]),
            amount=100000,
        )
        try:
            # print(request.POST.getlist('category'))
            drm_dest.save()
        except:
            DreamDestination.objects.filter(tms_owner=request.user).delete()
            drm_dest.save()

        sample_category = ast.literal_eval(DreamDestination.objects.all().filter(
            tms_owner=request.user).values_list('pCategory')[0][0])
        print(sample_category)
        print(type(sample_category))
        similarity_list = {}
        for i in range(0, len(PackageDetail.objects.all())):
            dest_category = ast.literal_eval(
                PackageDetail.objects.all().values_list('pCategory')[i][0])
            res = len(set(sample_category) & set(dest_category)) / \
                float(len(set(sample_category) | set(dest_category))) * 100
            similarity_list["{title}".format(
                title=PackageDetail.objects.all().values_list('pTitle')[i][0])] = res
        # print(similarity_list)
        sorted_similarity_list = {k: v for k, v in sorted(
            similarity_list.items(), key=lambda x: x[1], reverse=True)}
        recommended_destinations = list(sorted_similarity_list.keys())[0:6]
        # print(len(recommended_destinations))
        # print(dest_data[dest_data[1] == recommended_destinations[0]])
        RecommendedDestination_cat.objects.filter(
            recommendation_template=request.user.dreamdestination).delete()
        for recommended_destination in recommended_destinations:
            df = dest_data[dest_data[1] == recommended_destination]
            print(df.values[0][1])
            # print(dir(df[1]))
            rcm_dest = RecommendedDestination_cat(
                recommendation_template=request.user.dreamdestination,
                pTitle=df.values[0][1],
                pLocation=df.values[0][2],
                pdetails=df.values[0][3],
                pic=df.values[0][4],
                pCategory=df.values[0][5],
                amount=df.values[0][6],
            )
            rcm_dest.save()

        rcm_destinations_cat = RecommendedDestination_cat.objects.filter(
            recommendation_template=request.user.dreamdestination)
        # for i in range(10):
        #     recommended_destinations.append(sorted_similarity_list.values)

        # print(PackageDetail.objects.all().values_list('pTitle')[0][0])
        # print(type(ast.literal_eval(PackageDetail.objects.all().values_list('pCategory')[0][0])))
        context['rcm_destinations_cat'] = rcm_destinations_cat
        return render(request, 'home.html', context)
    else:
        return render(request, 'destination_options.html', context)

def DestinationRecommend_tags(request):
    context = {}
    
    if request.method == 'POST':
        sample_dest = pd.DataFrame(list(PackageDetail.objects.all().filter(pTitle=request.POST.get('des_title')).values_list(
        'pTitle', 'pLocation', 'pdetails', 'pic', 'pCategory', 'ptags','amount')))
        print(sample_dest)
        travel_data = pd.DataFrame(list(PackageDetail.objects.all().values_list(
        'pTitle', 'pLocation', 'pdetails', 'pic', 'pCategory', 'ptags','amount')))
        # display(travel_data[5])
        cv = CountVectorizer(max_features=5000,stop_words='english')
        vectors = cv.fit_transform(travel_data[5]).toarray()
        similarity = cosine_similarity(vectors)
        def recommend(dest):
            dest_index = travel_data[travel_data[0] == dest].index[0]
            distances = similarity[dest_index]
            dest_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
            print(dest_list)
            RecommendedDestination_tag.objects.filter(
            recommendation_template=request.user.dreamdestination).delete()
            for i in dest_list:
                print(travel_data.iloc[i[0]][3])
                rcm_dest = RecommendedDestination_tag(
                recommendation_template=request.user.dreamdestination,
                pTitle=travel_data.iloc[i[0]][0],
                pLocation=travel_data.iloc[i[0]][1],
                pdetails=travel_data.iloc[i[0]][2],
                pic=travel_data.iloc[i[0]][3],
                pCategory=travel_data.iloc[i[0]][4],
                amount=travel_data.iloc[i[0]][6],
                )
                rcm_dest.save()
        recommend(sample_dest[0][0])
        rcm_destinations = RecommendedDestination_tag.objects.filter(
            recommendation_template=request.user.dreamdestination)

        context["rcm_destinations"] = rcm_destinations
        context['sample_dest'] = sample_dest[0][0]
        
        return render(request, 'recommended_destinations_tag.html',context)
    else:
        return render(request, 'recommended_destinations_tag.html')
    # use concat instead of append cuz it'll be depreciated #it'll not be added again and again bcz dest data is being re initialized above.
    # print(sample_dest.columns)
    # dest_data = pd.concat([dest_data, sample_dest])
    # # keep these two below the concat..
    # display(dest_data.tail(5))
    # vectors_category = cv.fit_transform(dest_data[5].astype(str)).toarray()
    # category_similarity = cosine_similarity(vectors_category)
    # sorted(category_similarity[0], reverse=True)
    # sorted(
    #     list(enumerate(category_similarity[0])), reverse=True, key=lambda x: x[1])
    # cosine_similarity(vectors_category)
    # print("<<<<<<<<<<<<<<<<<<<<<< Cosine Similarity >>>>>>>>>>>>>>>>>>>>>>")

    # print(category_similarity)

    # # print(dir(request.user.dreamdestination.pTitle)) #str

    # def recommend_destinations(destination):
    #     print(destination)

    #     destination_index = dest_data[dest_data[1] == destination].index[0]
    #     print("<<<<<<<<<<<<<<<<<<<<<< Destination index >>>>>>>>>>>>>>>>>>>>>>")
    #     print(destination_index)
    #     print(dest_data[1])
    #     distances = category_similarity[destination_index]
    #     recommended_destinations = sorted(
    #         list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    #     print("<<<<<<<<<<<<<<<<<<<<<< Your selected Destination >>>>>>>>>>>>>>>>>>>>>>")
    #     display(dest_data[dest_data[1] == destination])
    #     print("<<<<<<<<<<<<<<<<<<<<<< Recommended Destinations >>>>>>>>>>>>>>>>>>>>")
    #     print(recommended_destinations)
    #     print("<<<<<<<<<<<<<<<<<<<<<< Deleting prev records >>>>>>>>>>>>>>>>>>>>")
    #     RecommendedDestination.objects.filter(
    #         recommendation_template=request.user.dreamdestination).delete()
    #     for i in recommended_destinations:
    #         display(dest_data.iloc[i[0]])
    #         rcm_dest = RecommendedDestination(
    #             recommendation_template=request.user.dreamdestination,
    #             pTitle=dest_data.iloc[i[0]][1],
    #             pLocation=dest_data.iloc[i[0]][2],
    #             pdetails=dest_data.iloc[i[0]][3],
    #             pic=dest_data.iloc[i[0]][4],
    #             pCategory=dest_data.iloc[i[0]][5],
    #             amount=dest_data.iloc[i[0]][6],
    #         )

    #         rcm_dest.save()

    #     print("<<<<<<<<<<<<<<<<<<<<<<<<< Saved in recommended_destinations   >>>>>>>>>>>>>>>>>>>>>>")

    #     rcm_destinations = RecommendedDestination.objects.filter(
    #         recommendation_template=request.user.dreamdestination)

    #     context["rcm_destinations"] = rcm_destinations

    #     # print(dir(request.user.dreamdestination.recommendeddestination_set))
    #     # print(dir(RecommendedDestination.objects.filter(recommendation_template=request.user.dreamdestination)[0]))
    #     # pass this in context dict.

    # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<< dream detination >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(request.user.dreamdestination.pTitle)
    # print(request.user.dreamdestination.pCategory)
    # recommend_destinations(request.user.dreamdestination.pTitle)
    
