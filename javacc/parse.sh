#blank count
BLANK=`find ./project/self/git_tool -name "*.java" |xargs cat|grep "^$"|wc -l`

#filter the code
find ./project/self/git_tool -name "*.java" |xargs cat |grep -v "^$"| cat > tmp.txt
java CommentStripParser tmp.txt > tmp2.txt

#code count
CODE=`sed 's/^[ \t]*//g' tmp2.txt|grep -v "^$"|wc -l`

#all count
ALL=`find ./project/self/git_tool -name "*.java" |xargs cat|wc -l`

#cal comment count
COMMENT=`expr $ALL - $CODE - $BLANK`

#print
echo 'blank:'$BLANK
echo 'code:'$CODE
echo 'comment:'$COMMENT
