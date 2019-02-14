% FileData = load('J:\\240\\project\\GANimation-20190112\\sample_dataset\\wiki.mat');
% csvwrite('J:\\240\\project\\GANimation-20190112\\sample_dataset\\wiki.csv', FileData.M);
%clear
%clc
FileData = load('wiki.mat');
x = FileData.wiki.dob;
count = 0;
for i = 1:length(FileData.wiki.dob)
    fprintf('%i\n', i)
    Dob = FileData.wiki.dob(i);
    Gender = FileData.wiki.gender(i);
    Photo_taken = FileData.wiki.photo_taken(i);
    Full_path = FileData.wiki.full_path(i);
    temp_age = datevec(datenum(Photo_taken,7,1)-Dob);
    Age = temp_age(1);
    columns = {'Dob', 'Gender', 'Photo_taken', 'Age'};
    temp_path = Full_path{1};
    data = table(Dob, Gender, Photo_taken, Age, 'VariableNames', columns);

    curr_path = strsplit(temp_path, '.');
    curr_path2 = strsplit(curr_path{1}, '/');
    file_name = strcat(curr_path2{2}, '.csv');
    prefix = strcat(curr_path2{1}, '_');%the prefix of the file name , number is the name of folder
    final_name = strcat(prefix, file_name)
    
    writetable(data, strcat('fuck/temp/', final_name));
    count = count + 1
    
end