from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


def Page(request, count_value, page_count):
    paginator = Paginator(count_value, page_count)
    if request.method == "GET":

        # 获取url后面的page参数的值，首页不显示，默认值为1
        page = request.GET.get("page")
        try:
            count_value = paginator.page(page)
        # 异常捕获
        except PageNotAnInteger:
            # 如果请求的首页不是整数，返回第一页
            count_value = paginator.page(1)
            pass
        except InvalidPage:
            # 如果请求的页数不是整数，放回第一页
            return HttpResponse('找不到页面')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            count_value = paginator.page(paginator.num_pages)
    return count_value

